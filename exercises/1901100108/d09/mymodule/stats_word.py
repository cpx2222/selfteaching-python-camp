from collections import Counter
# 统计参数中每个英文单词出现的次数
def stats_text_en(text, count):

    if not isinstance(text, str):
        raise ValueError('参数必须是str类型， 输入类型为%s' % type(text))

    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        # 用 str 类型 的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):

    if not isinstance(text, str):
        raise ValueError('参数必须是str类型， 输入类型为%s' % type(text))

    cn_characters = []
    for character in text:
        # unicode 中 中文 字符的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


def stats_text(text,count):
    '''
    合并 英文词频 和 中文字频 的结果
    '''
    
    if not isinstance(text, str):
        raise ValueError('参数必须是str类型， 输入类型为%s' % type(text))

    return Counter(text).most_common(count)


