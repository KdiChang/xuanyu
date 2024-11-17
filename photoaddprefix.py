import os
import re

# 定义正则表达式匹配 Markdown 文件中的图片链接
image_pattern = r'!\[(.*?)\]\((.*?)\)'

# 需要修改的前缀
prefix = '/docs'

# 遍历指定文件夹
def modify_image_paths_in_md(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 找到所有图片链接并在原有路径前添加前缀
                modified_content = re.sub(image_pattern, lambda match: f'![{match.group(1)}]({prefix}{match.group(2)})', content)

                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

                print(f"Modified: {file_path}")

# 使用函数
folder_path = '你的文件夹路径'
modify_image_paths_in_md(r"C:\Users\ChangjianPan\OneDrive - Kongsberg Digital AS\Desktop\实习总结\KM\hugo-KM\mysite\content\en\docs")
