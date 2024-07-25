import os
import re

# 定义要搜索的当前目录
current_directory = '.'  # 表示当前脚本运行的目录

# 正则表达式，用于匹配HTML文件
html_file_pattern = re.compile(r'.*\.html$', re.IGNORECASE)

# 定义替换函数
def replace_org_with_net(content):
    return re.sub(r'cdn.staticfile.org', 'cdn.staticfile.net', content)

# 遍历当前目录及其子目录下的所有文件
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if html_file_pattern.match(file):
            # 构建完整的文件路径
            file_path = os.path.join(root, file)
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 替换内容
            new_content = replace_org_with_net(content)
            # 将新内容写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated file: {file_path}')

print('Finished processing all HTML files.')