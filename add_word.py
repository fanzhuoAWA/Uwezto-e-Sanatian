#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
词典词条添加工具
版本: 3.0
"""

import os

def clear_screen():
    """清空屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """打印程序标题"""
    print("=" * 60)
    print("词典词条添加工具")
    print("=" * 60)
    print()

def get_required_input(prompt):
    """获取必填输入（不能为空）"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("此项为必填项，请输入内容！")

def get_optional_input(prompt, field_name="", default=""):
    """获取可选输入（可以回车跳过）"""
    hint = " (可选，直接回车跳过)" if field_name else ""
    value = input(f"{prompt}{hint}: ").strip()
    if value == "":
        return default
    return value

def get_part_of_speech_and_explanations():
    """获取词性和对应的释义"""
    while True:
        try:
            num_pos = input("请输入词性数量 (1-5，默认为1): ").strip()
            if num_pos == "":
                num_pos = 1
            else:
                num_pos = int(num_pos)
            
            if 1 <= num_pos <= 5:
                break
            else:
                print("请输入1-5之间的数字！")
        except ValueError:
            print("请输入有效的数字！")
    
    parts_of_speech = []
    explanations = []
    
    print()
    for i in range(1, num_pos + 1):
        print(f"词性 {i}:")
        pos = get_required_input(f"  请输入词性 (如: n., v., adj., onom.): ")
        parts_of_speech.append(pos)
        
        explanation = get_required_input(f"  请输入该词性的释义: ")
        explanations.append(explanation)
        print()
    
    return parts_of_speech, explanations

def get_example_sentences():
    """获取例句"""
    examples = []
    
    while True:
        try:
            num_examples = input("请输入例句数量 (0-10，默认为0): ").strip()
            if num_examples == "":
                num_examples = 0
            else:
                num_examples = int(num_examples)
            
            if 0 <= num_examples <= 10:
                break
            else:
                print("请输入0-10之间的数字！")
        except ValueError:
            print("请输入有效的数字！")
    
    if num_examples == 0:
        return examples
    
    print("\n现在请输入例句：")
    
    for i in range(1, num_examples + 1):
        print(f"\n例句 {i}:")
        original = get_required_input("  请输入例句原文: ")
        translation = get_optional_input("  请输入例句翻译", "例句翻译", "")
        
        if translation:
            examples.append(f"{original}###{translation}")
        else:
            examples.append(f"{original}###")
    
    return examples

def get_multiline_input(field_name):
    """获取多行输入"""
    notes = []
    print(f"请输入{field_name}，每行一条，输入空行结束：")
    
    line_num = 1
    while True:
        line = input(f"{line_num}> ").strip()
        if not line:
            break
        notes.append(line)
        line_num += 1
    
    return notes

def format_entry(entry_data):
    """格式化词条为文本格式"""
    lines = []
    
    lines.append("")

    # 必填项
    lines.append(f"word: {entry_data['word']}")
    lines.append(f"part_of_speech: {'@@@'.join(entry_data['part_of_speech'])}")
    lines.append(f"explanation: {'@@@'.join(entry_data['explanation'])}")
    
    # 可选项
    if entry_data['phonetic_symbols'] and entry_data['phonetic_symbols'] != "暂无":
        lines.append(f"phonetic_symbols: {entry_data['phonetic_symbols']}")
    else:
        lines.append(f"phonetic_symbols: 暂无")
    
    # 例句
    for i, example in enumerate(entry_data['examples'], 1):
        lines.append(f"example_sentence: {i}. {example}")
    
    # 语法注释
    if entry_data['grammar_notes']:
        for note in entry_data['grammar_notes']:
            lines.append(f"grammar_note: {note}")
    
    # 文化注释
    if entry_data['cultural_notes']:
        for note in entry_data['cultural_notes']:
            lines.append(f"cultural_note: {note}")
    
    

    return lines

def display_entry(entry_data):
    """显示词条信息用于检查"""
    print("=" * 60)
    print("请检查您输入的词条信息：")
    print("=" * 60)
    
    print(f"1. word（单词）: {entry_data['word']}")
    
    # 显示词性和释义
    print("2. part_of_speech（词性）和 explanation（释义）:")
    for i in range(len(entry_data['part_of_speech'])):
        pos = entry_data['part_of_speech'][i]
        exp = entry_data['explanation'][i] if i < len(entry_data['explanation']) else ""
        print(f"   词性 {i+1}: {pos}")
        print(f"     释义: {exp}")
    
    print(f"3. phonetic_symbols（音标）: {entry_data['phonetic_symbols'] if entry_data['phonetic_symbols'] else '无'}")
    
    # 显示例句
    print(f"4. examples（例句）:")
    if entry_data['examples']:
        for i, example in enumerate(entry_data['examples'], 1):
            if '###' in example:
                original, translation = example.split('###', 1)
                print(f"   例句 {i}:")
                print(f"     原文: {original}")
                print(f"     翻译: {translation if translation else '无'}")
            else:
                print(f"   例句 {i}: {example}")
    else:
        print(f"   无")
    
    # 显示语法注释
    print(f"5. grammar_notes（语法注释）:")
    if entry_data['grammar_notes']:
        for i, note in enumerate(entry_data['grammar_notes'], 1):
            print(f"   {i}. {note}")
    else:
        print(f"   无")
    
    # 显示文化注释
    print(f"6. cultural_notes（文化注释）:")
    if entry_data['cultural_notes']:
        for i, note in enumerate(entry_data['cultural_notes'], 1):
            print(f"   {i}. {note}")
    else:
        print(f"   无")
    
    print("=" * 60)

def modify_examples(examples):
    """修改例句"""
    while True:
        clear_screen()
        print("当前例句列表:")
        print("-" * 40)
        if not examples:
            print("暂无例句")
        else:
            for i, example in enumerate(examples, 1):
                if '###' in example:
                    original, translation = example.split('###', 1)
                    print(f"{i}. 原文: {original}")
                    print(f"   翻译: {translation if translation else '无'}")
                else:
                    print(f"{i}. {example}")
        
        print("\n操作选项:")
        print("  输入例句编号 (如: 1, 2, 3) 修改该例句")
        print("  输入 'd+编号' (如: d1, d2) 删除该例句")
        print("  输入 'a' 添加新例句")
        print("  输入 'y' 完成修改")
        
        action = input("\n请选择: ").strip().lower()
        
        if action == 'y':
            return examples
        elif action == 'a':
            print("\n添加新例句:")
            original = get_required_input("  请输入例句原文: ")
            translation = get_optional_input("  请输入例句翻译", "例句翻译", "")
            if translation:
                examples.append(f"{original}###{translation}")
            else:
                examples.append(f"{original}###")
        elif action.startswith('d'):
            # 删除例句
            try:
                index = int(action[1:]) - 1
                if 0 <= index < len(examples):
                    removed = examples.pop(index)
                    print(f"已删除例句: {removed}")
                else:
                    print("无效的例句编号！")
            except (ValueError, IndexError):
                print("格式错误！请输入如 'd1' 的格式")
            input("按回车键继续...")
        else:
            # 修改例句
            try:
                index = int(action) - 1
                if 0 <= index < len(examples):
                    print(f"\n修改例句 {index + 1}:")
                    if '###' in examples[index]:
                        current_original, current_translation = examples[index].split('###', 1)
                    else:
                        current_original = examples[index]
                        current_translation = ""
                    
                    print(f"当前原文: {current_original}")
                    new_original = get_optional_input("  请输入新原文 (回车保持原样)", "例句原文", current_original)
                    
                    print(f"当前翻译: {current_translation if current_translation else '无'}")
                    new_translation = get_optional_input("  请输入新翻译 (回车保持原样，输入 '-' 表示删除翻译)", "例句翻译", current_translation)
                    
                    if new_translation == '-':
                        examples[index] = f"{new_original}###"
                    elif new_translation:
                        examples[index] = f"{new_original}###{new_translation}"
                    else:
                        examples[index] = f"{new_original}###{current_translation}"
                        
                    print("例句已更新！")
                else:
                    print("无效的例句编号！")
            except ValueError:
                print("格式错误！请输入编号或 'd+编号'")
            input("按回车键继续...")

def modify_pos_and_expl(parts_of_speech, explanations):
    """修改词性和释义"""
    while True:
        clear_screen()
        print("当前词性和释义:")
        print("-" * 40)
        for i in range(len(parts_of_speech)):
            pos = parts_of_speech[i]
            exp = explanations[i] if i < len(explanations) else ""
            print(f"{i+1}. 词性: {pos}")
            print(f"    释义: {exp}")
        
        print("\n操作选项:")
        print("  输入编号 (如: 1, 2, 3) 修改该词性/释义")
        print("  输入 'a' 添加新词性/释义")
        print("  输入 'd+编号' (如: d1, d2) 删除该词性/释义")
        print("  输入 'y' 完成修改")
        
        action = input("\n请选择: ").strip().lower()
        
        if action == 'y':
            return parts_of_speech, explanations
        elif action == 'a':
            print("\n添加新词性和释义:")
            new_pos = get_required_input("  请输入新词性: ")
            new_exp = get_required_input("  请输入新释义: ")
            parts_of_speech.append(new_pos)
            explanations.append(new_exp)
        elif action.startswith('d'):
            # 删除词性/释义
            try:
                index = int(action[1:]) - 1
                if 0 <= index < len(parts_of_speech):
                    removed_pos = parts_of_speech.pop(index)
                    if index < len(explanations):
                        removed_exp = explanations.pop(index)
                    else:
                        removed_exp = ""
                    print(f"已删除: 词性 '{removed_pos}', 释义 '{removed_exp}'")
                else:
                    print("无效的编号！")
            except (ValueError, IndexError):
                print("格式错误！请输入如 'd1' 的格式")
            input("按回车键继续...")
        else:
            # 修改词性/释义
            try:
                index = int(action) - 1
                if 0 <= index < len(parts_of_speech):
                    print(f"\n修改词性/释义 {index + 1}:")
                    current_pos = parts_of_speech[index]
                    current_exp = explanations[index] if index < len(explanations) else ""
                    
                    print(f"当前词性: {current_pos}")
                    new_pos = get_optional_input("  请输入新词性 (回车保持原样)", "词性", current_pos)
                    
                    print(f"当前释义: {current_exp}")
                    new_exp = get_optional_input("  请输入新释义 (回车保持原样)", "释义", current_exp)
                    
                    parts_of_speech[index] = new_pos
                    if index < len(explanations):
                        explanations[index] = new_exp
                    else:
                        explanations.append(new_exp)
                        
                    print("已更新！")
                else:
                    print("无效的编号！")
            except ValueError:
                print("格式错误！请输入编号或 'd+编号'")
            input("按回车键继续...")

def modify_notes(notes, field_name):
    """修改注释（语法注释或文化注释）"""
    while True:
        clear_screen()
        print(f"当前{field_name}:")
        print("-" * 40)
        if not notes:
            print("暂无")
        else:
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note}")
        
        print(f"\n操作选项:")
        print(f"  输入编号 (如: 1, 2, 3) 修改该{field_name}")
        print(f"  输入 'a' 添加新{field_name}")
        print(f"  输入 'd+编号' (如: d1, d2) 删除该{field_name}")
        print(f"  输入 'y' 完成修改")
        
        action = input("\n请选择: ").strip().lower()
        
        if action == 'y':
            return notes
        elif action == 'a':
            print(f"\n添加新{field_name}:")
            new_note = get_required_input(f"  请输入新{field_name}: ")
            notes.append(new_note)
        elif action.startswith('d'):
            # 删除注释
            try:
                index = int(action[1:]) - 1
                if 0 <= index < len(notes):
                    removed = notes.pop(index)
                    print(f"已删除: {removed}")
                else:
                    print("无效的编号！")
            except (ValueError, IndexError):
                print("格式错误！请输入如 'd1' 的格式")
            input("按回车键继续...")
        else:
            # 修改注释
            try:
                index = int(action) - 1
                if 0 <= index < len(notes):
                    print(f"\n修改{field_name} {index + 1}:")
                    print(f"当前内容: {notes[index]}")
                    new_note = get_optional_input(f"  请输入新内容 (回车保持原样)", field_name, notes[index])
                    notes[index] = new_note
                    print("已更新！")
                else:
                    print("无效的编号！")
            except ValueError:
                print("格式错误！请输入编号或 'd+编号'")
            input("按回车键继续...")

def review_entry(entry_data):
    """让用户检查并修改词条"""
    while True:
        clear_screen()
        print_header()
        display_entry(entry_data)
        
        print("\n修改选项:")
        print("  1 - 修改 word（单词）")
        print("  2 - 修改 part_of_speech（词性）和 explanation（释义）")
        print("  3 - 修改 phonetic_symbols（音标）")
        print("  4 - 修改 examples（例句）")
        print("  5 - 修改 grammar_notes（语法注释）")
        print("  6 - 修改 cultural_notes（文化注释）")
        print("  y - 确认添加")
        
        action = input("\n请选择 (输入编号或 y): ").strip().lower()
        
        if action == 'y':
            return True
        elif action == '1':
            entry_data['word'] = get_required_input("请输入新的 word（单词）: ")
        elif action == '2':
            entry_data['part_of_speech'], entry_data['explanation'] = modify_pos_and_expl(
                entry_data['part_of_speech'], entry_data['explanation']
            )
        elif action == '3':
            entry_data['phonetic_symbols'] = get_optional_input("请输入新的 phonetic_symbols（音标）", "音标", entry_data['phonetic_symbols'])
        elif action == '4':
            entry_data['examples'] = modify_examples(entry_data['examples'])
        elif action == '5':
            entry_data['grammar_notes'] = modify_notes(entry_data['grammar_notes'], "语法注释")
        elif action == '6':
            entry_data['cultural_notes'] = modify_notes(entry_data['cultural_notes'], "文化注释")
        else:
            print(f"错误：未知的选择 '{action}'，请重新输入。")
            input("按回车键继续...")

def main():
    """主函数"""
    clear_screen()
    print_header()

    print("现在开始添加新的词典词条。")
    print()
    
    # 收集词条信息
    entry_data = {}
    
    # 必填项
    entry_data['word'] = get_required_input("1. word（单词）: ")
    
    # 词性和释义
    print()
    print("2. part_of_speech（词性）和 explanation（释义）:")
    entry_data['part_of_speech'], entry_data['explanation'] = get_part_of_speech_and_explanations()
    
    # 音标
    print("3. phonetic_symbols（音标，可选）:")
    entry_data['phonetic_symbols'] = get_optional_input("请输入音标 (如: /wɔːtə/)", "音标", "暂无")
    
    # 例句
    print()
    print("4. examples（例句）:")
    entry_data['examples'] = get_example_sentences()
    
    # 语法注释
    print()
    print("5. grammar_notes（语法注释，可选）:")
    entry_data['grammar_notes'] = get_multiline_input("语法注释")
    
    # 文化注释
    print()
    print("6. cultural_notes（文化注释，可选）:")
    entry_data['cultural_notes'] = get_multiline_input("文化注释")
    
    # 检查并确认
    if review_entry(entry_data):
        # 格式化并保存到文件
        formatted_lines = format_entry(entry_data)
        
        # 确保文件存在
        filename = "dictionary.txt"
        if not os.path.exists(filename):
            print(f"\n警告：{filename} 文件不存在，将创建新文件。")
        
        # 追加到文件
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write("\n".join(formatted_lines))
                # 在词条后面添加一个空行，确保词条之间有分隔
                f.write("\n")
            
            print(f"\n✓ 词条已成功添加到 {filename} 文件末尾！")
            print(f"共添加了 {len(formatted_lines)} 行内容。")
            
            # 显示添加的内容
            print("\n添加的内容：")
            print("-" * 40)
            for line in formatted_lines:
                print(line)
        
        except IOError as e:
            print(f"\n✗ 保存文件时出错: {e}")
            print("请确保文件没有被其他程序占用。")
    
    # 询问是否继续添加
    print("\n" + "=" * 60)
    continue_adding = input("\n是否继续添加另一个词条？(y/n): ").strip().lower()
    if continue_adding == 'y':
        main()
    else:
        print("\n感谢使用词典词条添加工具！")
        print("再见！")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断。")
    except Exception as e:
        print(f"\n程序出现错误: {e}")
        import traceback
        traceback.print_exc()