"""Проверка (и опционально установка) окружения для пайплайна саммари/перевода PDF.

    python install_libraries.py            # только проверка импортов
    python install_libraries.py --install  # доустановить пакеты, затем проверить
"""

import subprocess
import sys

PACKAGES = [
    "pymupdf",
    "pillow",
    "PyPDF2",
    "pdf2image",
    "langchain>=1.0",
    "langchain-core",
    "langchain-deepseek",
    "langchain-openai",
    "beautifulsoup4",
    "lxml",
    "pandas",
    "rich",
    "python-dotenv",
    "nest_asyncio",
    "aiofiles",
    "tqdm",
    "loguru",
    "playwright",
    "weasyprint",
    "pypdf",
    "paddlepaddle==3.0.0",
    "paddleocr>=3.0",
]


def install() -> None:
    if sys.version_info[:2] != (3, 11):
        print(f"ВНИМАНИЕ: Python {sys.version_info.major}.{sys.version_info.minor}, "
              f"ожидается 3.11 — paddlepaddle может не поставиться", flush=True)
    pip = [sys.executable, "-m", "pip", "install"]
    # cryptography ставим колесом заранее: иначе paddleocr тянет её из исходников
    # и падает на отсутствующем Rust-тулчейне
    subprocess.run(pip + ["--only-binary=:all:", "cryptography"], check=False)
    subprocess.run(pip + PACKAGES, check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=False)


if "--install" in sys.argv:
    install()

# ---------------------------------------------------------------- проверка
import pymupdf
from PIL import Image
import os
import shutil

import random
from langchain.tools import tool

from langchain_core.tools import BaseTool, tool
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.agents.middleware import ToolCallLimitMiddleware
from typing import Literal
from pathlib import Path
from typing import List
from langchain_openai import ChatOpenAI
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from rich import print as pprint
import base64
from dotenv import load_dotenv
load_dotenv()
CLOUD_API = os.getenv("CLOUD_API")
API_DEEPSEEK = os.getenv("API_DEEPSEEK")
import json
import re
import nest_asyncio
import asyncio
from typing import List, Any, Dict, Optional
import time
import PyPDF2

from functools import partial
import aiofiles

import sys
print(f'Python {sys.version}')

os.environ['FLAGS_use_mkldnn'] = '0'
os.environ['FLAGS_use_cinn'] = '0'
from pdf2image import convert_from_path

# Модули проекта, а не пакеты PyPI: вне каталога проекта их отсутствие — не ошибка.
try:
    from html_to_pdf_summary import html_to_pdf
    from html2pdf_latest import html_to_pdf as html_to_pdf_translation
    from merge_html_latest import merge_html_folder
    print("project modules: OK")
except ImportError as exc:
    print(f"project modules: недоступны ({exc.name}) — "
          f"запустите из корня проекта, если они нужны")

import paddle
paddle.set_device('cpu')
from paddleocr import PPStructureV3
from paddlex.inference.utils.io.writers import ImageWriter
from pathlib import Path
from typing import Union
from datetime import datetime, timedelta

from tqdm import tqdm
from loguru import logger as loguru_logger

import shutil

import warnings
warnings.filterwarnings('ignore')

print("libraries installation complete")
