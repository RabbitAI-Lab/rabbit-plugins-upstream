"""
Data Loader Module

Handles loading fund data from various sources:
- AKShare (online API)
- Local CSV files
- Historical analysis files
"""

import csv
import json
import os
from pathlib import Path
from datetime import datetime

# Try to import akshare
try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
except ImportError:
    AKSHARE_AVAILABLE = False


class DataLoader:
    def __init__(self, fund_code, fund_name, base_dir, today_dir):
        self.fund_code = fund_code
        self.fund_name = fund_name  # 可能来自用户输入，稍后可能被实际数据中的名称覆盖
        self.base_dir = base_dir
        self.today_dir = today_dir
        self.actual_fund_name = None  # 从实际数据中获取的基金名称
    
    def get_data_from_akshare(self):
        """从 akshare 获取基金数据"""
        if not AKSHARE_AVAILABLE:
            print("错误: akshare 不可用，请安装 akshare 库")
            return None
        
        try:
            print(f"从 akshare 获取基金 {self.fund_code} 数据...")
            
            # Strategy 1: ETF historical data (with OHLC)
            df = None
            data_source = None
            try:
                df_etf = ak.fund_etf_hist_sina(self.fund_code)
                if df_etf is not None and len(df_etf) > 0 and 'open' in df_etf.columns:
                    df = df_etf
                    data_source = 'fund_etf_hist_sina'
                    print(f"  使用 fund_etf_hist_sina 接口，获取{len(df)}条记录")
            except Exception as e1:
                print(f"  fund_etf_hist_sina 失败: {str(e1)[:100]}")
            
            # Strategy 2: Open-ended fund NAV data (only unit NAV)
            if df is None or len(df) == 0:
                try:
                    df_open = ak.fund_etf_fund_info_em(self.fund_code, start_date='20000101')
                    if df_open is not None and len(df_open) > 0:
                        df = df_open
                        data_source = 'fund_etf_fund_info_em'
                        print(f"  使用 fund_etf_fund_info_em 接口，获取{len(df)}条记录")
                        # 尝试从数据中获取基金名称
                        if self.actual_fund_name is None and len(df_open) > 0:
                            # 常见的基金名称字段名
                            name_columns = ['基金简称', '基金名称', '名称', 'name']
                            for col in name_columns:
                                if col in df_open.columns:
                                    self.actual_fund_name = str(df_open.iloc[0][col])
                                    print(f"  从数据中获取到基金名称: {self.actual_fund_name}")
                                    break
                        
                        # 如果无法获取名称，尝试使用 akshare 的 fund_info_ths 接口
                        if self.actual_fund_name is None:
                            try:
                                fund_info_df = ak.fund_info_ths(symbol=self.fund_code)
                                if fund_info_df is not None and len(fund_info_df) > 0:
                                    # 从 fund_info_ths 获取基金名称
                                    fund_full_name = fund_info_df.loc[fund_info_df['字段'] == '基金全称', '值'].values
                                    if len(fund_full_name) > 0 and fund_full_name[0] is not None:
                                        self.actual_fund_name = str(fund_full_name[0])
                                        print(f"  从 fund_info_ths 获取到基金名称: {self.actual_fund_name}")
                                    else:
                                        fund_short_name = fund_info_df.loc[fund_info_df['字段'] == '基金简称', '值'].values
                                        if len(fund_short_name) > 0 and fund_short_name[0] is not None:
                                            self.actual_fund_name = str(fund_short_name[0])
                                            print(f"  从 fund_info_ths 获取到基金简称: {self.actual_fund_name}")
                            except Exception as e:
                                print(f"  fund_info_ths 失败: {str(e)[:100]}")
                        
                        # 如果仍然无法获取名称，使用基金代码作为名称
                        if self.actual_fund_name is None:
                            self.actual_fund_name = f"基金代码: {self.fund_code} (名称未知)"
                            print(f"  无法获取基金名称，使用代码作为名称: {self.actual_fund_name}")
                except Exception as e2:
                    print(f"  fund_etf_fund_info_em 失败: {str(e2)[:100]}")
            
            if df is None or len(df) == 0:
                print(f"错误: 未能从 akshare 获取到 {self.fund_code} 的数据")
                return None
            
            # Convert to dictionary list
            data = []
            if data_source == 'fund_etf_hist_sina':
                for _, row in df.iterrows():
                    data.append({
                        'date': str(row['date']),
                        'open': float(row['open']),
                        'close': float(row['close']),
                        'high': float(row['high']),
                        'low': float(row['low']),
                        'volume': float(row['volume']) if 'volume' in row and row['volume'] is not None else 0
                    })
            elif data_source == 'fund_etf_fund_info_em':
                for _, row in df.iterrows():
                    nav = float(row['单位净值'])
                    data.append({
                        'date': str(row['净值日期']),
                        'open': nav,
                        'close': nav,
                        'high': nav,
                        'low': nav,
                        'volume': 0
                    })
            
            # Save raw data
            raw_data_path = self.today_dir / f"raw_data_akshare_{data_source}.json"
            with open(raw_data_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'source': data_source,
                    'fund_code': self.fund_code,
                    'fetch_time': datetime.now().isoformat(),
                    'records': data
                }, f, ensure_ascii=False, indent=2)
            
            # Convert to internal format
            parsed_data = []
            for item in data:
                parsed_data.append({
                    'date': datetime.strptime(item['date'], '%Y-%m-%d'),
                    'open': item['open'],
                    'close': item['close'],
                    'high': item['high'],
                    'low': item['low'],
                    'volume': item['volume']
                })
            
            return parsed_data
            
        except Exception as e:
            print(f"从 akshare 获取数据失败: {e}")
            return None
    
    def load_data_from_csv(self, csv_path):
        """从 CSV 文件加载数据"""
        data = []
        try:
            with open(csv_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
                    row['open'] = float(row['open'])
                    row['close'] = float(row['close'])
                    row['high'] = float(row['high'])
                    row['low'] = float(row['low'])
                    data.append(row)
            return sorted(data, key=lambda x: x['date'])
        except Exception as e:
            print(f"加载 CSV 数据失败: {e}")
            return None
    
    def load_historical_analysis(self):
        """加载历史分析结果"""
        historical_analysis = []
        
        # Find root-level historical analysis (backward compatibility)
        base_path = os.environ.get('FUND_ANALYSIS_BASE_PATH', 'investment_analysis')
        root_analysis_file = Path('.') / base_path / f"{self.fund_code}_analysis.md"
        if root_analysis_file.exists():
            try:
                with open(root_analysis_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                mod_time = os.path.getmtime(root_analysis_file)
                date_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
                historical_analysis.append({
                    'date': date_str,
                    'content': content
                })
            except:
                pass
        
        # Find historical analysis in date subdirectories
        if self.base_dir.exists():
            for date_dir in sorted(self.base_dir.iterdir()):
                if date_dir.is_dir() and date_dir.name != self.today_dir.name:
                    analysis_file = date_dir / f"{self.fund_code}_analysis.md"
                    if analysis_file.exists():
                        try:
                            with open(analysis_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            historical_analysis.append({
                                'date': date_dir.name,
                                'content': content
                            })
                        except:
                            pass
        
        return historical_analysis