"""
Chart Generator Module

Generates charts for fund analysis reports using matplotlib.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.font_manager as fm


class ChartGenerator:
    def __init__(self, fund_code, fund_name, output_dir):
        self.fund_code = fund_code
        self.fund_name = fund_name
        self.output_dir = output_dir
        
        # 设置中文字体 - 使用更稳健的方法
        self._setup_chinese_font()
    
    def _setup_chinese_font(self):
        """设置中文字体以避免乱码"""
        # 获取所有可用字体
        try:
            mat_fonts = set([f.name for f in fm.fontManager.ttflist])
        except:
            mat_fonts = set()
        
        # 特殊处理WenQuanYi字体（它们是.ttc文件）
        wenquanyi_fonts = [f for f in fm.fontManager.ttflist if 'wenquanyi' in f.name.lower()]
        if wenquanyi_fonts:
            # 使用第一个WenQuanYi字体
            try:
                font_name = wenquanyi_fonts[0].name
                plt.rcParams['font.sans-serif'] = [font_name]
                # 测试字体是否可用
                fig, ax = plt.subplots(figsize=(1, 1))
                ax.text(0.5, 0.5, '测试', fontsize=12)
                plt.close(fig)
                print(f"信息: 使用中文字体: {font_name}")
                # 确保负号正确显示
                plt.rcParams['axes.unicode_minus'] = False
                return
            except Exception as e:
                print(f"警告: 无法使用WenQuanYi字体: {e}")
        
        # 优先使用的中文字体列表（排除WenQuanYi，因为我们已经尝试过了）
        preferred_chinese_fonts = [
            'WenQuanYi Micro Hei',    # 文泉驿微米黑
            'SimHei',                 # 黑体
            'Microsoft YaHei',        # 微软雅黑
            'Noto Sans CJK SC',       # 思源黑体
            'Source Han Sans CN'      # 思源黑体
            'Heiti TC'
        ]
        
        # 尝试设置字体
        font_set = False
        for font in preferred_chinese_fonts:
            if font in mat_fonts:
                try:
                    plt.rcParams['font.sans-serif'] = [font]
                    # 测试字体是否可用
                    fig, ax = plt.subplots(figsize=(1, 1))
                    ax.text(0.5, 0.5, '测试', fontsize=12)
                    plt.close(fig)
                    font_set = True
                    print(f"信息: 使用中文字体: {font}")
                    break
                except:
                    continue
        
        if not font_set:
            # 后备方案 - 尝试使用系统可能有的任何中文字体
            chinese_fonts = [f for f in mat_fonts if any(keyword in f.lower() for keyword in 
                           ['hei', 'song', 'kai', 'fang', 'yahei', 'noto', 'source', 'cjk', 'zh'])]
            if chinese_fonts:
                try:
                    plt.rcParams['font.sans-serif'] = [chinese_fonts[0]]
                    # 测试字体是否可用
                    fig, ax = plt.subplots(figsize=(1, 1))
                    ax.text(0.5, 0.5, '测试', fontsize=12)
                    plt.close(fig)
                    font_set = True
                    print(f"信息: 使用中文字体: {chinese_fonts[0]}")
                except:
                    pass
        
        if not font_set:
            # 最后的后备方案
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
            print("警告: 未找到合适的中文字体，图表中的中文可能显示为方框")
        
        # 确保负号正确显示
        plt.rcParams['axes.unicode_minus'] = False
    
    def generate_annual_return_chart(self, stats, filename=None):
        """
        生成年度收益率走势图
        
        Args:
            stats: 年度统计数据列表，每个元素包含 year, return 等字段
            filename: 输出文件名，默认为 {fund_code}_annual_return.png
        
        Returns:
            str: 生成的图表文件路径
        """
        if not stats:
            return None
        
        if filename is None:
            filename = f"{self.fund_code}_annual_return.png"
        
        # 提取数据
        years = [s['year'] for s in stats]
        returns = [s['return'] for s in stats]
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # 绘制柱状图 - 根据中国市场惯例：红色表示上涨(正收益)，绿色表示下跌(负收益)
        colors = ['red' if r >= 0 else 'green' for r in returns]
        bars = ax.bar(years, returns, color=colors, alpha=0.7, edgecolor='black')
        
        # 添加数值标签
        for i, (bar, ret) in enumerate(zip(bars, returns)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{ret:.1f}%',
                   ha='center', va='bottom' if ret >= 0 else 'top',
                   fontsize=9)
        
        # 添加零线
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        # 设置标题和标签
        ax.set_title(f'{self.fund_name} ({self.fund_code}) 年度收益率走势', 
                     fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('年份', fontsize=11)
        ax.set_ylabel('收益率 (%)', fontsize=11)
        
        # 设置x轴刻度
        ax.set_xticks(years)
        ax.set_xticklabels(years, rotation=45)
        
        # 添加网格
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # 计算统计信息
        avg_return = sum(returns) / len(returns)
        positive_years = sum(1 for r in returns if r > 0)
        
        # 添加统计文本
        textstr = f'平均年化: {avg_return:.2f}%\n正收益年份: {positive_years}/{len(years)}'
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        
        # 保存图表
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        return str(filepath)
    
    def generate_annual_high_low_chart(self, stats, filename=None):
        """
        生成年度高低点走势图
        
        Args:
            stats: 年度统计数据列表
            filename: 输出文件名
        
        Returns:
            str: 生成的图表文件路径
        """
        if not stats:
            return None
        
        if filename is None:
            filename = f"{self.fund_code}_annual_high_low.png"
        
        # 提取数据
        years = [s['year'] for s in stats]
        highs = [s['high'] for s in stats]
        lows = [s['low'] for s in stats]
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # 绘制高点和低点线
        ax.plot(years, highs, 'o-', color='red', linewidth=2, markersize=6, label='年度高点')
        ax.plot(years, lows, 'o-', color='green', linewidth=2, markersize=6, label='年度低点')
        
        # 填充高低点之间的区域
        ax.fill_between(years, lows, highs, alpha=0.2, color='gray')
        
        # 设置标题和标签
        ax.set_title(f'{self.fund_name} ({self.fund_code}) 年度高低点走势', 
                     fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('年份', fontsize=11)
        ax.set_ylabel('价格', fontsize=11)
        
        # 设置x轴刻度
        ax.set_xticks(years)
        ax.set_xticklabels(years, rotation=45)
        
        # 添加图例
        ax.legend(loc='best', fontsize=10)
        
        # 添加网格
        ax.grid(alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        
        # 保存图表
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        return str(filepath)

    def generate_monthly_volatility_chart(self, monthly_stats, filename=None):
        """
        生成月度波动模式图
        
        Args:
            monthly_stats: 月度统计数据列表，每个元素包含 month (YYYY-MM), volatility, return 等
            filename: 输出文件名，默认为 {fund_code}_monthly_volatility.png
        
        Returns:
            str: 生成的图表文件路径
        """
        if not monthly_stats:
            return None
        
        if filename is None:
            filename = f"{self.fund_code}_monthly_volatility.png"
        
        # 按月份号聚合数据（跨年平均）
        month_data = {i: {'volatility': [], 'return': []} for i in range(1, 13)}
        for stat in monthly_stats:
            # month 格式如 '2023-01'
            month_num = int(stat['month'].split('-')[1])
            month_data[month_num]['volatility'].append(stat['volatility'])
            month_data[month_num]['return'].append(stat['return'])
        
        # 计算平均值
        months = list(range(1, 13))
        avg_volatility = []
        avg_return = []
        for m in months:
            vol_list = month_data[m]['volatility']
            ret_list = month_data[m]['return']
            avg_volatility.append(sum(vol_list) / len(vol_list) if vol_list else 0)
            avg_return.append(sum(ret_list) / len(ret_list) if ret_list else 0)
        
        # 创建图表
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # 绘制月度平均波动幅度柱状图
        bars = ax1.bar(months, avg_volatility, alpha=0.5, color='blue', label='平均波动幅度')
        ax1.set_xlabel('月份', fontsize=11)
        ax1.set_ylabel('平均波动幅度 (%)', fontsize=11, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        ax1.set_xticks(months)
        ax1.set_xticklabels([f'{m}月' for m in months])
        
        # 创建第二个Y轴绘制月度平均收益率折线图 - 突出显示
        ax2 = ax1.twinx()
        ax2.plot(months, avg_return, 'o-', color='#D35400', linewidth=3, markersize=8, 
                 markeredgecolor='white', markeredgewidth=1.5, label='平均收益率')
        ax2.set_ylabel('平均收益率 (%)', fontsize=11, color='#D35400')
        ax2.tick_params(axis='y', labelcolor='#D35400')
        
        # 添加数值标签到柱状图
        for i, (bar, vol) in enumerate(zip(bars, avg_volatility)):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{vol:.1f}%',
                    ha='center', va='bottom', fontsize=8, color='blue')
        
        # 添加数值标签到折线图
        for i, (ret) in enumerate(avg_return):
            ax2.text(months[i], ret,
                    f'{ret:.1f}%',
                    ha='center', va='bottom' if ret >= 0 else 'top',
                    fontsize=9, fontweight='bold', color='#D35400',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        
        # 设置标title
        ax1.set_title(f'{self.fund_name} ({self.fund_code}) 月度波动模式图', 
                     fontsize=14, fontweight='bold', pad=15)
        
        # 添加图例（合并两个轴的图例）
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=10, framealpha=0.9)
        
        # 添加网格
        ax1.grid(alpha=0.3, linestyle='--', axis='y')
        
        plt.tight_layout()
        
        # 保存图表
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        return str(filepath)

    def generate_wave_trend_chart(self, data, waves, filename=None):
        """
        生成波段走势图，标注波段类型
        
        Args:
            data: 基金数据列表，包含日期和净值等信息
            waves: 波段分析结果，来自 wave_analyzer.analyze_waves()
            filename: 输出文件名，默认为 {fund_code}_wave_trend.png
        
        Returns:
            str: 生成的图表文件路径
        """
        if not data or not waves:
            return None
        
        if filename is None:
            filename = f"{self.fund_code}_wave_trend.png"
        
        # 提取日期和净值数据
        dates = [d['date'] for d in data]
        prices = [d['close'] for d in data]  # 使用收盘价作为净值
                
        # 创建图表
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # 绘制净值走势线
        ax.plot(dates, prices, linewidth=2, color='black', label='基金净值')
        
        # 获取波段统计数据
        wave_stats = waves.get('wave_stats', [])
        current_wave = waves.get('current_wave')
        pivot_points = waves.get('pivot_points', [])
        
        # 标记转折点（支撑点和压力点）
        pivot_highs = [p for p in pivot_points if p['type'] == 'high']
        pivot_lows = [p for p in pivot_points if p['type'] == 'low']
        
        if pivot_highs:
            high_dates = [p['date'] for p in pivot_highs]
            high_prices = [p['price'] for p in pivot_highs]
            ax.scatter(high_dates, high_prices, color='red', s=60, zorder=5, 
                      marker='v', label='压力点')
        
        if pivot_lows:
            low_dates = [p['date'] for p in pivot_lows]
            low_prices = [p['price'] for p in pivot_lows]
            ax.scatter(low_dates, low_prices, color='green', s=60, zorder=5, 
                      marker='^', label='支撑点')
        
        # 为每个完成的波段添加背景颜色和标注
        for i, wave in enumerate(wave_stats):
            start_date = wave['start_date']
            end_date = wave['end_date']
            
            # 确保日期是datetime对象
            if isinstance(start_date, str):
                start_dt = datetime.strptime(start_date, '%Y-%m-%d')
            else:
                start_dt = start_date
            if isinstance(end_date, str):
                end_dt = datetime.strptime(end_date, '%Y-%m-%d')
            else:
                end_dt = end_date
            
            # 根据波段类型设置背景颜色
            if wave['wave_type'] == 'up':
                # 上升波段：淡红色背景
                ax.axvspan(start_dt, end_dt, alpha=0.2, color='red', label='上升波段' if i == 0 else "")
                # 添加波段类型文字标注
                mid_date = start_dt + (end_dt - start_dt) / 2
                mid_price = (prices[dates.index(start_dt)] + prices[dates.index(end_dt)]) / 2
                ax.text(mid_date, mid_price, '上升波段', 
                       ha='center', va='center', fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
            else:  # down
                # 下降波段：淡绿色背景
                ax.axvspan(start_dt, end_dt, alpha=0.2, color='green', label='下降波段' if i == 0 else "")
                # 添加波段类型文字标注
                mid_date = start_dt + (end_dt - start_dt) / 2
                mid_price = (prices[dates.index(start_dt)] + prices[dates.index(end_dt)]) / 2
                ax.text(mid_date, mid_price, '下降波段', 
                       ha='center', va='center', fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
        
        # 处理当前进行中的波段（如果有）
        if current_wave and current_wave.get('wave_type') != 'initial':
            start_date = current_wave['start_date']
            end_date = dates[-1]  # 到今天
            
            # 确保日期是datetime对象
            if isinstance(start_date, str):
                start_dt = datetime.strptime(start_date, '%Y-%m-%d')
            else:
                start_dt = start_date
            # end_date 已经是 datetime 对象（来自 dates 列表）
            end_dt = end_date
            
            # 根据当前波段类型设置背景颜色
            if current_wave['wave_type'] == 'up':
                ax.axvspan(start_dt, end_dt, alpha=0.3, color='red', label='当前上升波段')
                mid_date = start_dt + (end_dt - start_dt) / 2
                mid_price = (prices[dates.index(start_dt)] + prices[-1]) / 2
                ax.text(mid_date, mid_price, '当前上升波段', 
                       ha='center', va='center', fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.9))
            else:  # down
                ax.axvspan(start_dt, end_dt, alpha=0.3, color='green', label='当前下降波段')
                mid_date = start_dt + (end_dt - start_dt) / 2
                mid_price = (prices[dates.index(start_dt)] + prices[-1]) / 2
                ax.text(mid_date, mid_price, '当前下降波段', 
                       ha='center', va='center', fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.9))
        
        # 设置图表标题和标签
        ax.set_title(f'{self.fund_name} ({self.fund_code}) 波段走势图', 
                     fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('日期', fontsize=12)
        ax.set_ylabel('净值 (元)', fontsize=12)
        
        # 设置日期格式
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # 每3个月一个主刻度
        plt.xticks(rotation=45)
        
        # 添加图例
        ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
        
        # 添加网格
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # 添加统计信息文本框
        total_waves = waves.get('total_waves', 0)
        current_drawdown = waves.get('current_drawdown', 0)
        
        stats_text = f'历史波段数: {total_waves}\n当前回撤: {current_drawdown:.2f}%'
        if current_wave and current_wave.get('wave_type') != 'initial':
            stats_text += f'\n当前波段: {current_wave.get("status", "未知")}'
        
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
        
        plt.tight_layout()
        
        # 保存图表
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        return str(filepath)
