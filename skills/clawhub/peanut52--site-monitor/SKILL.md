---
name: site-monitor
description: Monitor websites for uptime and content changes. Use when checking if a URL is online, detecting page modifications, or tracking HTTP status codes over time.
homepage: https://github.com/yourname/site-monitor
user-invocable: true
metadata:
  openclaw:
    os:
      - linux
    requires:
      bins:
        - python3
---

# Site Monitor

网站存活与内容变更监控技能。它通过定期请求目标 URL 并对比页面内容哈希，帮助用户发现网站宕机或内容被篡改的情况。

## Overview

- **What it does:** 检查 URL 是否可访问；记录网页内容 MD5 哈希；对比历史快照以检测页面是否变化。
- **When to use it:** 当用户要求"检查某个网站是否在线"、"监控页面是否更新"、"定期检测站点状态"时使用。
- **Requirements:** Python 3 环境，`requests` 库已安装。

## Quick start

### Install

技能自带脚本 `scripts/monitor.py`，依赖 Python 3 和 `requests` 库：

```bash
pip3 install requests
