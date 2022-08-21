'''
Author: liuyin
Date: 2022-08-22 00:55:12
LastEditTime: 2022-08-22 00:55:12
FilePath: /scripts/wordle-helper/main.py
Description: 
'''


import argparse
from dynaconf import loaders
from dynaconf.utils.boxing import DynaBox
from dynaconf import Dynaconf

# from gooey import Gooey, GooeyParser

# 配置
CONFIG_FILE = 'config.toml'
conf = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[CONFIG_FILE],
)


def load_dictionary():
    f = open(conf.DICT_FILE)
    words = []
    word = f.readline()
    while word:
        words.append(word.split("\n")[0])
        word = f.readline()
    f.close()
    return words


# 更新配置文件
def update_config(conf):
    # conf[key] = value
    data = conf.as_dict()
    loaders.write(CONFIG_FILE, DynaBox(data).to_dict())

# 初始化配置文件,开始新游戏


def new_game(length):
    print("开始新游戏")
    getRandomWord(length)
    conf.WORD_LENGTH = length
    print("已设置单词长度为:{}".format(conf.WORD_LENGTH))
    # 初始化其他配置
    conf.NO_LETTERS = []
    conf.GUESSED_LETTERS = {}
    conf.ERR_POS_LETTERS = {}
    update_config(conf)

    print("初始化配置文件:{}".format(CONFIG_FILE))


def getRandomWord(word_length):
    words = load_dictionary()
    for w in words:
        # 返回符合长度并且无重复字母的单词
        if len(w) == len(set(w)) == int(word_length):
            print("随机生成的单词为:{}".format(w))
            return
    else:
        # 否则返回符合长度的单词
        for w in words:
            if len(w) == int(word_length):
                print("随机生成的单词为:{}".format(w))
                return
        print("未找到符合长度 {} 的单词".format(word_length))


def add_no_letters(value):
    no_letters = conf.NO_LETTERS
    for l in value:
        if l not in no_letters:
            no_letters.append(l)
    conf.NO_LETTERS = no_letters
    update_config(conf)
    print("已添加不能使用的字母:{}".format(value))


def add_guessed_letter(value):
    print(value)
    new_values = []
    guessed_letter = conf.GUESSED_LETTERS
    if ',' in value:
        new_values = value.split(',')
    else:
        new_values = [value]
    print(new_values)
    for g in new_values:
        if len(g) < 2:
            print("输入错误:{}".format(g))
        else:
            letter = g[0]
            pos = int(str(g)[1:])
            # print(letter, pos)
            letters = list(guessed_letter.keys())
            # print(type(letters[0]), type(letter))
            if letter not in letters:
                print("{} 新字母".format(letter))
                guessed_letter[letter] = pos
            else:
                print("{} 已经存在了,更新pos".format(letter))
                guessed_letter[letter] = pos

    conf.GUESSED_LETTERS = guessed_letter
    update_config(conf)
    print("添加已猜中的字母:{}".format(value))


def add_err_pos_letter(value):
    print(value)
    new_values = []
    err_pos_letter = conf.ERR_POS_LETTERS
    if ',' in value:
        new_values = value.split(',')
    else:
        new_values = [value]
    print(new_values)
    for g in new_values:
        if len(g) < 2:
            print("输入错误:{}".format(g))
        else:
            letter = g[0]
            pos = int(str(g)[1:])
            # print(letter, pos)
            letters = list(err_pos_letter.keys())
            # print(type(letters[0]), type(letter))
            if letter not in letters:
                print("{} 新字母".format(letter))
                err_pos_letter[letter] = [pos]
            else:
                print("{} 已经存在了".format(letter))
                print(err_pos_letter[letter])
                pos_list = list(err_pos_letter[letter])

                pos_list.append(pos)
                err_pos_letter[letter] = list(set(pos_list))
    conf.ERR_POS_LETTERS = err_pos_letter
    update_config(conf)
    print("添加已猜中的字母:{}".format(value))
# 从词库中筛选指定长度的单词


def filter_by_length(words):
    filtered_words = []
    for w in words:
        if len(w) == conf.WORD_LENGTH:
            filtered_words.append(w)
    return filtered_words
# 从词库中筛选不包含指定字母的单词


def filter_no_letters(words):
    filtered_words = []
    no_letters = conf.NO_LETTERS
    for w in words:
        # 计算差集,如果返回等于no_letters,则说明没有重复字母
        diff = set(no_letters).difference(set(list(w)))
        if diff == set(no_letters):
            # print(w, no_letters)
            filtered_words.append(w)

    return filtered_words
# 筛选猜对位置字母的单词


def filter_guessed_Letter(words):
    filtered_words = []
    data = conf.GUESSED_LETTERS
    if len(data) == 0:
        return words
    else:
        for w in words:
            if [False for l in list(data.keys()) if l not in w]:
                words.remove(w)
                continue
            if len([True for l in list(data.keys())
                    if data[l] == list(w).index(l)+1]) == len(data):
                filtered_words.append(w)
                continue
    return filtered_words


def filter_err_pos_letter(words):
    filtered_words = []
    data = conf.ERR_POS_LETTERS
    if len(data) == 0:
        return words
    else:
        letters = list(data.keys())
        for w in words:
            tag = False
            for l in letters:
                if l in w:
                    pos = list(w).index(l)+1
                    if pos in data[l]:
                        tag = False
                        break
                    else:
                        tag = True
                else:
                    break
            if tag:
                filtered_words.append(w)
                continue
    return filtered_words


def start():
    words = load_dictionary()
    print("本地词典共{}个单词".format(len(words)))
    words = filter_by_length(words)
    print("筛选出长度为 {} 的单词 {} 个,".format(conf.WORD_LENGTH, len(words)))
    # 从词库中筛选不包含指定字母的单词 - 灰色
    words = filter_no_letters(words)
    print("筛选不包含指定字母 {} 的单词,共 {} 个".format(conf.NO_LETTERS, len(words)))
    # 筛选已知位置字母的单词 -- 绿色
    words = filter_guessed_Letter(words)
    print("筛选猜对位置字母 {} 的单词,共 {} 个".format(conf.GUESSED_LETTERS, len(words)))
    # 筛选已知存在但位置不对的单词 -- 黄色
    words = filter_err_pos_letter(words)
    print("筛选已知存在但位置不对的字母 {} 的单词,共 {} 个".format(
        conf.ERR_POS_LETTERS, len(words)))
    print("可选单词列表:{}".format(words))


def set_word_length(length):
    conf.WORD_LENGTH = length
    print("修改单词长度为:{}".format(length))
    update_config(conf)


# @Gooey()
def main():
    parser = argparse.ArgumentParser(description='binance 猜字游戏')
    parser.add_argument("-new", "--new",  help="开始新游戏并指定单词长度", type=int)
    parser.add_argument("-l", "--length", help="设置单词长度", type=int)
    parser.add_argument("-n", "--noletter", help="添加不包含的字母")
    parser.add_argument("-g", "--guessed_letter", help="添加已猜中的字母")
    parser.add_argument("-e", "--error_pos_letter", help="添加已知存在但位置错误的字母")
    args = parser.parse_args()
    if args.new:
        new_game(args.new)
        return
    elif args.length:
        set_word_length(args.length)
    elif args.noletter:
        add_no_letters(args.noletter)
    elif args.guessed_letter:
        add_guessed_letter(args.guessed_letter)
    elif args.error_pos_letter:
        add_err_pos_letter(args.error_pos_letter)
    else:
        start()


if __name__ == "__main__":
    main()
