"""
Base Analyzer Module

Contains the main FundAnalyzer class that coordinates all analysis components.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from analyzer.data_loader import DataLoader
from analyzer.annual_analysis import AnnualAnalyzer
from analyzer.wave_analysis import WaveAnalyzer
from analyzer.monthly_analysis import MonthlyAnalyzer
from analyzer.seasonal_analysis import SeasonalAnalyzer
from analyzer.holding_analysis import HoldingAnalyzer
from analyzer.report_generator import ReportGenerator
from utils.file_utils import ensure_directories, save_report, save_raw_data
from utils.date_utils import parse_date, format_date, days_between, estimate_trading_days


class FundAnalyzer:
    def __init__(self, fund_code, fund_name):
        self.fund_code = fund_code
        # 优先使用从数据源获取的实际基金名称，如果不可用则使用用户提供的名称，最后回退到基金代码
        self.fund_name = fund_name if fund_name else fund_code
        # Use relative paths based on current working directory or skill location
        # Default to ./investment_analysis/<fund_code>/ but allow override via env var
        base_path = os.environ.get('FUND_ANALYSIS_BASE_PATH', 'investment_analysis')
        self.base_dir = Path(base_path) / fund_code
        self.today_dir = self.base_dir / datetime.now().strftime("%Y-%m-%d")
        
        # Initialize analyzers
        self.data_loader = None
        self.annual_analyzer = AnnualAnalyzer()
        self.wave_analyzer = WaveAnalyzer()
        self.monthly_analyzer = MonthlyAnalyzer()
        self.seasonal_analyzer = SeasonalAnalyzer()
        self.holding_analyzer = HoldingAnalyzer()
        self.report_generator = ReportGenerator()
    
    def ensure_directories(self):
        """确保目录结构存在"""
        self.base_dir, self.today_dir = ensure_directories(
            os.environ.get('FUND_ANALYSIS_BASE_PATH', 'investment_analysis'), 
            self.fund_code
        )
        return self.today_dir
    
    def get_data_from_akshare(self):
        """从 akshare 获取基金数据"""
        # Initialize data loader if needed
        if self.data_loader is None:
            self.ensure_directories()
            self.data_loader = DataLoader(
                self.fund_code, 
                self.fund_name, 
                self.base_dir, 
                self.today_dir
            )
        return self.data_loader.get_data_from_akshare()
    
    def load_data_from_csv(self, csv_path):
        """从 CSV 文件加载数据"""
        if self.data_loader is None:
            self.ensure_directories()
            self.data_loader = DataLoader(
                self.fund_code, 
                self.fund_name, 
                self.base_dir, 
                self.today_dir
            )
        return self.data_loader.load_data_from_csv(csv_path)
    
    def load_historical_analysis(self):
        """加载历史分析结果"""
        if self.data_loader is None:
            self.ensure_directories()
            self.data_loader = DataLoader(
                self.fund_code, 
                self.fund_name, 
                self.base_dir, 
                self.today_dir
            )
        return self.data_loader.load_historical_analysis()
    
    def analyze(self, use_akshare=False, csv_path=None):
        """执行完整分析流程"""
        # 确保目录存在
        self.ensure_directories()
        
        # 加载数据
        if use_akshare:
            data = self.get_data_from_akshare()
            # 如果从akshare获取了数据，尝试使用实际的基金名称
            if self.data_loader and self.data_loader.actual_fund_name:
                self.fund_name = self.data_loader.actual_fund_name
        elif csv_path:
            data = self.load_data_from_csv(csv_path)
        else:
            print("错误: 必须指定数据来源 (--use-akshare 或 --csv-path)")
            return None
        
        if data is None or len(data) == 0:
            print("错误: 无法获取基金数据")
            return None
        
        print(f"加载完成，共{len(data)}条记录")
        
        # 加载历史分析
        historical_analysis = self.load_historical_analysis()
        if historical_analysis:
            print(f"找到{len(historical_analysis)}个历史分析记录")
        else:
            print("找到0个历史分析记录")
        
        # 执行各项分析
        print("年度分析...")
        stats = self.annual_analyzer.analyze_annual(data)
        print(f"分析完成，共{len(stats)}年数据")
        
        print("生成报告...")
        report = self.report_generator.generate_report(
            self.fund_code, 
            self.fund_name, 
            data, 
            stats, 
            historical_analysis,
            self.wave_analyzer,
            self.monthly_analyzer,
            self.seasonal_analyzer,
            self.holding_analyzer,
            self.today_dir  # 传递输出目录用于生成图表
        )
        print(f"DEBUG: Report length before saving: {len(report)} characters")
        print(f"DEBUG: Report ends with: {repr(report[-200:])}")
        
        # 保存报告
        report_file = save_report(
            report, 
            self.base_dir, 
            self.fund_code, 
            "_akshare" if use_akshare else ("_csv" if csv_path else "")
        )
        
        # 保存原始数据（如果是从akshare获取的）
        if use_akshare:
            # 这里我们需要从data_loader获取source信息，但为了简化，我们假设是akshare
            save_raw_data(
                [{'date': d['date'].strftime('%Y-%m-%d'), 
                  'open': d['open'], 
                  'close': d['close'], 
                  'high': d['high'], 
                  'low': d['low'], 
                  'volume': d['volume']} for d in data],
                'akshare',
                self.fund_code,
                self.base_dir
            )
        
        print(f"报告已保存至: {report_file}")
        return report