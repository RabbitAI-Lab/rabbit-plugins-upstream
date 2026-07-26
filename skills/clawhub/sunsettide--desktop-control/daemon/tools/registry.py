"""
AI Tool Registry — tool declarations + executor for LLM Function Calling.

Architecture:
  - Each tool is declared with a JSON Schema for its parameters.
  - tools_list returns all tool declarations (OpenAI/Anthropic compatible format).
  - tools_call routes LLM function_call payloads to actual handler functions.

The registry is populated at daemon startup and held in memory.
"""
import json
import traceback
from typing import Any, Callable, Dict, List, Optional


# ── Tool Schema Definitions ────────────────────────────────────────────────

TOOL_DEFINITIONS = [
    # --- Vision-based tools ---
    {
        "type": "function",
        "function": {
            "name": "find_text",
            "description": "在屏幕上搜索指定文字，返回所有匹配位置的坐标和边界框。适用于定位按钮、标签等界面元素。",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "要搜索的文字（支持中文/英文）"},
                    "region": {"type": "object", "description": "可选，限定搜索区域 {left, top, width, height}。不传则全屏搜索。"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号（默认 0 = 主屏幕）"},
                    "lang": {"type": "string", "description": "可选，OCR 语言（默认 chi_sim+eng）"},
                    "exact_match": {"type": "boolean", "description": "是否精确匹配（默认 true），false 支持包含匹配"},
                    "limit": {"type": "integer", "description": "返回结果数量上限（默认 10）"},
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "click_text",
            "description": "在屏幕上找到指定文字并点击它。适用于点击按钮、链接、菜单项等。",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "要点击的文字"},
                    "region": {"type": "object", "description": "可选，限定搜索区域"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                    "button": {"type": "string", "enum": ["left", "right", "middle"], "description": "鼠标按键"},
                    "click_type": {"type": "string", "enum": ["single", "double"], "description": "单击或双击"},
                    "offset": {"type": "object", "description": "相对文字中心点的偏移 {x, y}"},
                    "wait": {"type": "number", "description": "点击前等待秒数"},
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "type_to_text",
            "description": "在屏幕上找到指定文字附近的位置，点击聚焦后输入文本。适用于在'用户名'标签下方输入账号等场景。",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "作为定位锚点的文字"},
                    "input": {"type": "string", "description": "要输入的内容"},
                    "anchor": {"type": "string", "enum": ["above", "below", "left", "right"], "description": "相对于锚点的方位（默认 below）"},
                    "offset": {"type": "object", "description": "额外的坐标偏移 {x, y}"},
                    "clear_first": {"type": "boolean", "description": "输入前是否全选删除（默认 true）"},
                    "press_enter": {"type": "boolean", "description": "输入后是否按回车（默认 false）"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                },
                "required": ["text", "input"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mouse_smart_action",
            "description": "执行一系列文字驱动的鼠标动作（悬停、点击、移动、拖拽）。适用于菜单操作如'文件→保存'。",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "初始文字目标"},
                    "actions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string", "enum": ["hover", "click", "move_to", "drag", "wait"]},
                                "text": {"type": "string", "description": "目标文字"},
                                "button": {"type": "string", "description": "鼠标按键"},
                                "duration": {"type": "number", "description": "悬停/等待时间"},
                            },
                        },
                        "description": "动作链列表",
                    },
                },
                "required": ["actions"],
            },
        },
    },
    # --- Basic tools ---
    {
        "type": "function",
        "function": {
            "name": "mouse_move",
            "description": "移动鼠标到指定坐标。",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "integer", "description": "X 坐标"},
                    "y": {"type": "integer", "description": "Y 坐标"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                },
                "required": ["x", "y"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mouse_click",
            "description": "在当前位置或指定坐标点击鼠标。",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "integer", "description": "可选，X 坐标（不传则在当前位置点击）"},
                    "y": {"type": "integer", "description": "可选，Y 坐标"},
                    "button": {"type": "string", "enum": ["left", "right", "middle"], "description": "鼠标按键"},
                    "clicks": {"type": "integer", "description": "点击次数（1=单击，2=双击）"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "keyboard_type",
            "description": "输入文本。支持中英文混排、智能空格。",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "要输入的文本"},
                    "smart_space": {"type": "boolean", "description": "自动在中英文之间插入空格"},
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "keyboard_press",
            "description": "按下并释放一个键。用于输入 enter、tab、escape 等特殊键。",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "键名：enter, tab, escape, backspace, delete, f1-f12, up, down, left, right, space 等"},
                    "times": {"type": "integer", "description": "按下次数的简写"},
                },
                "required": ["key"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "keyboard_hotkey",
            "description": "执行键盘快捷键，如 Ctrl+C、Alt+Tab 等。",
            "parameters": {
                "type": "object",
                "properties": {
                    "keys": {"type": "array", "items": {"type": "string"}, "description": "按键组合列表，如 ['ctrl', 'c']"},
                },
                "required": ["keys"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "window_focus",
            "description": "查找窗口标题并聚焦到前台。适用于打开/切换到某个应用程序。",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "窗口标题（支持部分匹配）"},
                },
                "required": ["title"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "window_list",
            "description": "列出所有打开的窗口。适用于了解当前运行了哪些程序。",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "screenshot_save",
            "description": "截取屏幕或区域并保存到文件。",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "保存路径"},
                    "region": {"type": "object", "description": "可选，截取区域 {left, top, width, height}"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "screen_ocr",
            "description": "识别屏幕或指定区域的文字。",
            "parameters": {
                "type": "object",
                "properties": {
                    "region": {"type": "object", "description": "可选，识别区域 {left, top, width, height}"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                    "lang": {"type": "string", "description": "OCR 语言（默认 chi_sim+eng）"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "screen_context",
            "description": "获取当前屏幕的文字摘要，包括所有可识别的文字及其位置。适用于 AI 了解屏幕上正在显示什么。",
            "parameters": {
                "type": "object",
                "properties": {
                    "region": {"type": "object", "description": "可选，分析的屏幕区域"},
                    "monitor": {"type": "integer", "description": "可选，显示器编号"},
                    "lang": {"type": "string", "description": "OCR 语言"},
                    "include_layout": {"type": "boolean", "description": "是否包含文字布局信息"},
                    "max_chars": {"type": "integer", "description": "最多返回字符数（默认 2000）"},
                },
            },
        },
    },
]


def list_tools():
    """Return all tool declarations in OpenAI Function Calling format."""
    return {"tools": TOOL_DEFINITIONS}
