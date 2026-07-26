---
name: competitor-price-monitor
description: 自动监控竞品价格，生成价格趋势报告。当用户说"监控竞品价格"、"追踪价格变化"、"价格监控"、"竞品分析"时触发此技能。支持淘宝、京东、拼多多、亚马逊等主流电商平台。
---

# 竞品价格监控器 (Competitor Price Monitor)

## 概述

本技能自动监控指定竞品的价格变化，生成价格趋势分析报告，帮助商家优化定价策略。

**核心价值**：
- ⏱️ 节省时间：手动2小时 → 自动5分钟
- 📊 数据驱动：实时价格数据 + 趋势分析
- 💰 优化定价：基于竞品价格调整策略
- 🔔 及时预警：价格异常自动通知

## 使用场景

- 电商卖家需要监控竞品价格
- 品牌方需要追踪渠道价格
- 采购需要监控原材料价格
- 消费者需要追踪商品价格变化

## 完整工作流

### 输入 → 输出

```
输入：产品关键词 或 产品URL列表
输出：价格监控报告（Markdown/Excel/腾讯文档）
```

### 工作流程详解

#### 第1步：配置监控列表

**输入格式**（JSON文件）：
```json
{
  "products": [
    {
      "name": "iPhone 15 Pro Max",
      "platforms": ["taobao", "jd", "pdd"],
      "urls": {
        "taobao": "https://item.taobao.com/...",
        "jd": "https://item.jd.com/...",
        "pdd": "https://mobile.yangkeduo.com/..."
      }
    }
  ]
}
```

**保存位置**：`config/monitor_list.json`

---

#### 第2步：抓取价格数据

**工具**：`xbrowser` 技能（浏览器自动化）

**支持的电商平台**：
1. **淘宝/天猫** - 使用 `item.taobao.com`
2. **京东** - 使用 `item.jd.com`
3. **拼多多** - 使用 `mobile.yangkeduo.com`
4. **亚马逊** - 使用 `amazon.com`
5. **抖音电商** - 使用 `haohuo.jinritemai.com`

**示例脚本**（保存到 `scripts/scrape_price.py`）：
```python
import json
import subprocess
from datetime import datetime

def scrape_price(product_url, platform):
    """使用xbrowser抓取价格"""
    
    # 构建xbrowser命令
    cmd = [
        'python', '-m', 'xbrowser',
        '--url', product_url,
        '--platform', platform,
        '--action', 'get_price',
        '--output', 'json'
    ]
    
    # 执行命令
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        data = json.loads(result.stdout)
        return {
            'price': data.get('price'),
            'currency': data.get('currency', 'CNY'),
            'availability': data.get('availability', 'unknown'),
            'scraped_at': datetime.now().isoformat()
        }
    else:
        print(f"Error scraping {product_url}: {result.stderr}")
        return None

def scrape_multiple_products(products):
    """批量抓取产品价格"""
    results = []
    
    for product in products:
        product_name = product['name']
        urls = product.get('urls', {})
        
        for platform, url in urls.items():
            print(f"Scraping {product_name} on {platform}...")
            price_data = scrape_price(url, platform)
            
            if price_data:
                results.append({
                    'product': product_name,
                    'platform': platform,
                    'price': price_data['price'],
                    'currency': price_data['currency'],
                    'availability': price_data['availability'],
                    'url': url,
                    'scraped_at': price_data['scraped_at']
                })
    
    return results

if __name__ == '__main__':
    # 读取监控列表
    with open('config/monitor_list.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # 抓取价格
    results = scrape_multiple_products(config['products'])
    
    # 保存结果
    output_file = f"output/prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 价格数据已保存：{output_file}")
```

---

#### 第3步：数据分析与趋势判断

**分析维度**：
1. **价格对比** - 同一产品在不同平台的价格
2. **价格趋势** - 历史价格变化曲线
3. **价格波动** - 最大/最小/平均价格
4. **促销识别** - 判断是否正在促销

**示例脚本**（保存到 `scripts/analyze_prices.py`）：
```python
import json
import pandas as pd
from datetime import datetime

def analyze_prices(price_data):
    """分析价格数据"""
    
    # 转换为DataFrame
    df = pd.DataFrame(price_data)
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    
    # 按产品和平台分组
    analysis = []
    
    for (product, platform), group in df.groupby(['product', 'platform']):
        prices = group['price'].tolist()
        
        analysis.append({
            'product': product,
            'platform': platform,
            'current_price': prices[-1] if prices else None,
            'min_price': min(prices) if prices else None,
            'max_price': max(prices) if prices else None,
            'avg_price': sum(prices) / len(prices) if prices else None,
            'price_change': prices[-1] - prices[0] if len(prices) > 1 else 0,
            'scraped_at': group['scraped_at'].max()
        })
    
    return analysis

def generate_report(analysis, output_format='markdown'):
    """生成分析报告"""
    
    if output_format == 'markdown':
        report = "# 竞品价格监控报告\n\n"
        report += f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        for item in analysis:
            report += f"## {item['product']} - {item['platform']}\n\n"
            report += f"- 当前价格：{item['current_price']} {item['currency']}\n"
            report += f"- 最低价：{item['min_price']} {item['currency']}\n"
            report += f"- 最高价：{item['max_price']} {item['currency']}\n"
            report += f"- 平均价：{item['avg_price']:.2f} {item['currency']}\n"
            report += f"- 价格变化：{item['price_change']} {item['currency']}\n"
            report += f"- 更新时间：{item['scraped_at']}\n\n"
        
        return report
    
    elif output_format == 'excel':
        # 使用xlsx技能生成Excel报告
        pass

if __name__ == '__main__':
    # 读取价格数据
    import glob
    price_files = glob.glob('output/prices_*.json')
    if not price_files:
        print("No price data found!")
        exit(1)
    
    latest_file = max(price_files)
    with open(latest_file, 'r', encoding='utf-8') as f:
        price_data = json.load(f)
    
    # 分析价格
    analysis = analyze_prices(price_data)
    
    # 生成报告
    report = generate_report(analysis, output_format='markdown')
    
    # 保存报告
    output_file = f"output/price_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 分析报告已生成：{output_file}")
```

---

#### 第4步：保存报告

**支持的输出格式**：
1. **Markdown** - 保存到本地
2. **Excel** - 使用 `xlsx` 技能
3. **腾讯文档** - 使用 `tencent-docs` 技能（需要授权）
4. **邮件** - 使用 `imap-smtp-email` 技能

---

## 定时自动化

配合 `qclaw-cron-skill` 实现每日自动监控：

```json
{
  "name": "每日价格监控",
  "schedule": {
    "kind": "cron",
    "expr": "0 9,15,21 * * *",
    "tz": "Asia/Shanghai"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "使用 competitor-price-monitor 技能，抓取竞品价格并生成报告"
  },
  "sessionTarget": "isolated",
  "delivery": {
    "mode": "announce"
  }
}
```

以上配置会在每天9点、15点、21点自动执行价格监控。

---

## 变现路径

### 1. 在ClawHub上销售此Skill

**定价建议**：
- 基础版：199元（只能监控5个产品）
- 专业版：499元（无限产品 + 历史数据）
- 企业版：1999元（API接口 + 定制开发）

### 2. 提供价格监控服务

**服务收费**：
- 按月订阅：299元/月（监控10个产品）
- 按季度订阅：799元/季度
- 按年订阅：2999元/年

---

## 资源文件

### scripts/

- `scrape_price.py`：价格抓取脚本
- `analyze_prices.py`：价格分析脚本
- `generate_report.py`：报告生成脚本

### config/

- `monitor_list.json`：监控列表配置文件
- `platform_config.json`：电商平台配置

### references/

- `platform_api.md`：各平台价格抓取方法
- `anti_scraping.md`：反爬虫策略应对

---

**提示**：初次使用可以先不创建脚本，直接让我按照工作流程执行即可。熟悉后可以根据需要逐步添加资源文件。

---
## 💰 付费增值服务

想要更省事？我还提供：

| 服务 | 价格 | 内容 |
|------|------|------|
| 🚗 代安装调试 | ¥68/次 | 帮你安装配置，解决环境问题 |
| 🛠️ 定制技能开发 | ¥200起 | 根据需求开发专属技能 |
| 🚀 视频自动化陪跑 | ¥999/月 | 从0到1搭建完整视频自动化 |
| 📦 技能全家桶 | ¥199 | 11个AI技能永久用 + 代安装 |

**微信咨询**：[微信号待填写]

---
