# typer 移除 click 传递依赖模式

## 根因

typer 0.26.7 移除了 click 作为传递依赖。但很多项目直接 import click（不通过 typer）。

## 典型症状

```
ModuleNotFoundError: No module named 'click'
```

## 检查方法

```bash
# 检查项目是否直接 import click
grep -r "from click import\|import click" --include="*.py" .
# 检查 pyproject.toml/setup.py 是否声明了 click
grep "click" pyproject.toml setup.py requirements.txt
```

## 修复

在 pyproject.toml 的 dependencies 中加 `click`：

```toml
dependencies = [
    "typer>=0.9.0",
    "click>=8.0.0",  # 直接依赖，不再依赖 typer 传递
]
```

## 已知受影响项目

- TheR1D/shell_gpt #771 (12.1k stars)
- 可能还有更多使用 typer + 直接 import click 的项目

## 搜索查询

```bash
gh search issues "click" "typer" "missing" --language python --state open --limit 10 --sort created
```
