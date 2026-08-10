# 章节标题识别正则表达式模式库

## 中文图书章节模式

### 基础章节模式
```python
# 第X章格式
r'^第[一二三四五六七八九十百千万]+章[^\n]*$'
r'^第[0-9]+章[^\n]*$'

# 第X节格式  
r'^第[一二三四五六七八九十百千万]+节[^\n]*$'
r'^第[0-9]+节[^\n]*$'

# 第X篇格式
r'^第[一二三四五六七八九十百千万]+篇[^\n]*$'
r'^第[0-9]+篇[^\n]*$'
```

### 扩展章节模式
```python
# 带副标题的章节
r'^第[一二三四五六七八九十百千万]+章[：:][^\n]+$'
r'^第[0-9]+章[：:][^\n]+$'

# 带括号的章节
r'^\([一二三四五六七八九十百千万]+\)[^\n]*$'
r'^\([0-9]+\)[^\n]*$'

# 中文数字章节
r'^[一二三四五六七八九十百千万]+\.[^\n]*$'
r'^[一二三四五六七八九十百千万]+、[^\n]*$'
```

## 英文图书章节模式

### 基础英文模式
```python
# Chapter格式
r'^Chapter\s+[0-9IVXLCDM]+[^\n]*$'
r'^CHAPTER\s+[0-9IVXLCDM]+[^\n]*$'

# Part格式
r'^Part\s+[0-9IVXLCDM]+[^\n]*$'
r'^PART\s+[0-9IVXLCDM]+[^\n]*$'

# Section格式
r'^Section\s+[0-9]+[^\n]*$'
r'^SECTION\s+[0-9]+[^\n]*$'
```

### 扩展英文模式
```python
# 带标题的章节
r'^Chapter\s+[0-9IVXLCDM]+:\s*[^\n]+$'
r'^Part\s+[0-9IVXLCDM]+:\s*[^\n]+$'

# 罗马数字章节
r'^[IVXLCDM]+\.\s*[^\n]+$'
r'^[IVXLCDM]+\s+[^\n]+$'

# 字母章节
r'^[A-Z]+\.\s*[^\n]+$'
r'^Appendix\s+[A-Z][^\n]*$'
```

## 数字编号模式

### 多级编号
```python
# 一级编号
r'^[0-9]+\.[^\n]*$'

# 二级编号  
r'^[0-9]+\.[0-9]+[^\n]*$'
r'^[0-9]+\.[0-9]+\.[^\n]*$'

# 三级编号
r'^[0-9]+\.[0-9]+\.[0-9]+[^\n]*$'
r'^[0-9]+\.[0-9]+\.[0-9]+\.[^\n]*$'
```

### 括号编号
```python
# 圆括号编号
r'^\([0-9]+\)[^\n]*$'
r'^\([0-9]+\.[0-9]+\)[^\n]*$'

# 方括号编号
r'^\[[0-9]+\][^\n]*$'
r'^\[[0-9]+\.[0-9]+\][^\n]*$'
```

## 学术论文模式

### 论文章节
```python
# 摘要、关键词等
r'^[摘要|关键词|Abstract|Keywords|引言|结论|参考文献][^\n]*$'

# 学术章节
r'^[0-9]+\s*[引言|文献综述|研究方法|实验结果|讨论|结论][^\n]*$'

# 图表标题
r'^图\s*[0-9]+[^\n]*$'
r'^表\s*[0-9]+[^\n]*$'
r'^Figure\s*[0-9]+[^\n]*$'
r'^Table\s*[0-9]+[^\n]*$'
```

## 技术文档模式

### 技术章节
```python
# 技术文档章节
r'^[0-9]+\s*[概述|简介|背景|目标|范围][^\n]*$'
r'^[0-9]+\s*[安装|配置|部署][^\n]*$'
r'^[0-9]+\s*[使用指南|操作说明][^\n]*$'
r'^[0-9]+\s*[故障排除|常见问题][^\n]*$'

# API文档
r'^[GET|POST|PUT|DELETE|PATCH]\s+[^\n]+$'
r'^/api/[^\n]+$'
r'^[0-9]+\.[0-9]+\s+接口[^\n]*$'
```

## 小说文学作品模式

### 小说章节
```python
# 卷篇章节
r'^第[一二三四五六七八九十百千万]+卷[^\n]*$'
r'^第[一二三四五六七八九十百千万]+部[^\n]*$'

# 回目格式（传统小说）
r'^第[一二三四五六七八九十百千万]+回[^\n]*$'
r'^[0-9]+回[^\n]*$'

# 现代小说章节
r'^[一二三四五六七八九十百千万]+、[^\n]+$'
r'^Chapter\s*[0-9]+[^\n]*$'
```

## 混合模式匹配策略

### 优先级排序
```python
# 高优先级：明确的章节标记
PRIORITY_HIGH = [
    r'^第[一二三四五六七八九十百千万]+章[^\n]*$',
    r'^Chapter\s+[0-9IVXLCDM]+[^\n]*$',
]

# 中优先级：数字编号
PRIORITY_MEDIUM = [
    r'^[0-9]+\.[0-9]+[^\n]*$',
    r'^第[0-9]+章[^\n]*$',
]

# 低优先级：可能的章节
PRIORITY_LOW = [
    r'^[0-9]+\s+[^\n]{5,30}$',
    r'^[A-Z]+\.[^\n]{5,30}$',
]
```

### 上下文验证
```python
def validate_chapter_title(line, prev_lines, next_lines):
    """
    验证章节标题的有效性
    
    Args:
        line: 当前行
        prev_lines: 前面几行
        next_lines: 后面几行
    
    Returns:
        是否为有效的章节标题
    """
    # 检查行长度（章节标题通常较短）
    if len(line) > 50:
        return False
    
    # 检查前后内容（章节标题前后通常有空白）
    if prev_lines and prev_lines[-1].strip():
        # 如果前面一行有内容，检查是否是页码等噪音
        if re.match(r'^\d+$', prev_lines[-1].strip()):
            return True
        return False
    
    # 检查后面内容（章节标题后应该有正文）
    if next_lines and not next_lines[0].strip():
        return False
    
    # 检查字体特征（如果可用）
    # OCR通常不保留字体信息，这里只是示例
    
    return True
```

## 特殊情况处理

### 假阳性排除
```python
# 排除页码
r'^-\s*\d+\s*-'
r'^第\s*\d+\s*页'

# 排除版权信息
r'^[版权所有|Copyright|©]'
r'^[ISBN|ISSN]'
r'^[出版|Publish]'

# 排除页眉页脚
r'^.*机密.*$'
r'^.*内部资料.*$'
r'^Confidential'
```

### 跨页章节标题
```python
def handle_cross_page_titles(pages):
    """
    处理跨页的章节标题
    
    Args:
        pages: 页面列表
    
    Returns:
        处理后的页面列表
    """
    for i in range(len(pages) - 1):
        current_last_line = pages[i][-1].strip()
        next_first_line = pages[i+1][0].strip()
        
        # 检查是否是跨页的章节标题
        if (is_potential_chapter_start(current_last_line) and 
            is_potential_chapter_continuation(next_first_line)):
            
            # 合并跨页标题
            full_title = current_last_line + next_first_line
            
            # 更新页面内容
            pages[i][-1] = full_title
            pages[i+1] = pages[i+1][1:]  # 移除下一页的第一行
    
    return pages
```

## 动态模式学习

### 从文档中学习模式
```python
def learn_chapter_patterns(document):
    """
    从文档中学习章节标题模式
    
    Args:
        document: 文档内容
    
    Returns:
        学习到的模式列表
    """
    # 统计重复出现的格式
    pattern_counter = Counter()
    
    lines = document.split('\n')
    for line in lines:
        line = line.strip()
        if is_potential_chapter(line):
            # 提取模式特征
            pattern = extract_pattern_features(line)
            pattern_counter[pattern] += 1
    
    # 选择高频模式
    learned_patterns = [
        pattern for pattern, count in pattern_counter.most_common(5)
        if count >= 3  # 至少出现3次
    ]
    
    return learned_patterns
```

## 实际应用示例

### 完整的章节识别流程
```python
def identify_chapters(document):
    """
    完整的章节识别流程
    
    Args:
        document: 文档内容
    
    Returns:
        章节列表
    """
    # 1. 预定义模式匹配
    predefined_matches = match_with_predefined_patterns(document)
    
    # 2. 学习文档特定模式
    learned_patterns = learn_chapter_patterns(document)
    learned_matches = match_with_learned_patterns(document, learned_patterns)
    
    # 3. 合并结果
    all_matches = merge_matches(predefined_matches, learned_matches)
    
    # 4. 上下文验证
    validated_matches = validate_with_context(all_matches, document)
    
    # 5. 排除假阳性
    final_matches = exclude_false_positives(validated_matches)
    
    return final_matches
```