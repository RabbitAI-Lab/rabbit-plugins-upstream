#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
竞品价格监控器 - 主程序
功能：自动监控竞品价格，生成价格趋势报告
作者：QClaw AI
创建时间：2026-06-12
"""

import os
import json
import subprocess
from datetime import datetime
import time

class CompetitorPriceMonitor:
    """竞品价格监控器主类"""
    
    def __init__(self, config_dir='config', output_dir='output'):
        """初始化监控器"""
        self.config_dir = config_dir
        self.output_dir = output_dir
        
        # 创建目录
        os.makedirs(config_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)
        
        # 加载配置
        self.monitor_list = self._load_monitor_list()
        
        print(" price monitor initialized")
        print(f"📁 Config directory: {os.path.abspath(config_dir)}")
        print(f"📁 Output directory: {os.path.abspath(output_dir)}")
        print(f"📊 Monitoring {len(self.monitor_list)} products")
    
    def _load_monitor_list(self):
        """加载监控列表"""
        config_file = os.path.join(self.config_dir, 'monitor_list.json')
        
        if not os.path.exists(config_file):
            # 创建示例配置
            example_config = {
                "products": [
                    {
                        "name": "iPhone 15 Pro Max",
                        "platforms": ["jd", "taobao"],
                        "urls": {
                            "jd": "https://item.jd.com/100058382528.html",
                            "taobao": "https://item.taobao.com/item.htm?id=123456"
                        }
                    }
                ]
            }
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(example_config, f, ensure_ascii=False, indent=2)
            
            print(f"📝 Created example config: {config_file}")
            return example_config['products']
        
        else:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get('products', [])
    
    def scrape_price(self, product_name, platform, url):
        """抓取单个产品价格"""
        print(f"  Scraping {product_name} on {platform}...")
        
        try:
            # 使用xbrowser抓取价格
            # 注意：这里是简化版本，实际需要调用xbrowser技能
            cmd = [
                'python', '-m', 'xbrowser',
                '--url', url,
                '--action', 'get_price',
                '--output', 'json'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return {
                    'product': product_name,
                    'platform': platform,
                    'price': data.get('price'),
                    'currency': data.get('currency', 'CNY'),
                    'availability': data.get('availability', 'unknown'),
                    'url': url,
                    'scraped_at': datetime.now().isoformat()
                }
            else:
                print(f"    ⚠️  Failed to scrape {url}")
                return None
        
        except Exception as e:
            print(f"    ❌ Error scraping {url}: {e}")
            return None
    
    def scrape_all(self):
        """抓取所有产品价格"""
        print(f"\n🔍 Starting price scraping...")
        
        results = []
        
        for product in self.monitor_list:
            product_name = product['name']
            urls = product.get('urls', {})
            
            for platform, url in urls.items():
                price_data = self.scrape_price(product_name, platform, url)
                if price_data:
                    results.append(price_data)
                
                # 避免请求过快
                time.sleep(2)
        
        # 保存结果
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(self.output_dir, f'prices_{timestamp}.json')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Price data saved: {output_file}")
        return output_file
    
    def analyze_prices(self, price_data_file):
        """分析价格数据"""
        print(f"\n📊 Analyzing price data...")
        
        with open(price_data_file, 'r', encoding='utf-8') as f:
            price_data = json.load(f)
        
        # 简化分析：按产品分组，计算统计信息
        analysis = {}
        
        for item in price_data:
            product = item['product']
            platform = item['platform']
            
            if product not in analysis:
                analysis[product] = {}
            
            analysis[product][platform] = {
                'current_price': item['price'],
                'currency': item['currency'],
                'availability': item['availability'],
                'scraped_at': item['scraped_at']
            }
        
        # 保存分析结果
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(self.output_dir, f'analysis_{timestamp}.json')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Analysis saved: {output_file}")
        return output_file
    
    def generate_report(self, analysis_file):
        """生成Markdown报告"""
        print(f"\n📝 Generating report...")
        
        with open(analysis_file, 'r', encoding='utf-8') as f:
            analysis = json.load(f)
        
        # 生成Markdown报告
        report = "# 竞品价格监控报告\n\n"
        report += f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        report += "---\n\n"
        
        for product, platforms in analysis.items():
            report += f"## {product}\n\n"
            
            for platform, data in platforms.items():
                report += f"### {platform}\n\n"
                report += f"- **当前价格**: {data['price']} {data['currency']}\n"
                report += f"- **库存状态**: {data['availability']}\n"
                report += f"- **更新时间**: {data['scraped_at']}\n\n"
            
            report += "---\n\n"
        
        # 保存报告
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(self.output_dir, f'report_{timestamp}.md')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Report generated: {output_file}")
        return output_file
    
    def run(self):
        """完整流程：抓取 → 分析 → 报告"""
        print(f"\n{'='*60}")
        print(f"🚀 Starting Competitor Price Monitor")
        print(f"{'='*60}")
        
        # 第1步：抓取价格
        price_data_file = self.scrape_all()
        
        # 第2步：分析数据
        analysis_file = self.analyze_prices(price_data_file)
        
        # 第3步：生成报告
        report_file = self.generate_report(analysis_file)
        
        print(f"\n{'='*60}")
        print(f"🎉 Price monitoring completed!")
        print(f"{'='*60}")
        print(f"📄 Report: {report_file}")
        print(f"{'='*60}\n")
        
        return report_file


def main():
    """主函数"""
    monitor = CompetitorPriceMonitor()
    report_file = monitor.run()
    print(f"✅ Success! Report: {report_file}")


if __name__ == '__main__':
    main()
