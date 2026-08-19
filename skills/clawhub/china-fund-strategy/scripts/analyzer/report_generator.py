"""
Report Generator Module

Generates the full analysis report in Markdown format,
integrating results from all analysis modules.
"""

from datetime import datetime, timedelta
from utils.chart_generator import ChartGenerator


class ReportGenerator:
    def generate_report(self, fund_code, fund_name, data, stats, historical_analysis,
                        wave_analyzer=None, monthly_analyzer=None,
                        seasonal_analyzer=None, holding_analyzer=None,
                        output_dir=None):
        """生成完整分析报告"""
        report = []
        
        # 初始化图表生成器
        chart_generator = None
        if output_dir:
            chart_generator = ChartGenerator(fund_code, fund_name, output_dir)
            path_replaced = str(output_dir.parent)

        # ===== 标题 =====
        report.append(f"# {fund_name} ({fund_code}) 投资分析报告")
        report.append(f"**分析日期**: {datetime.now().strftime('%Y-%m-%d')}")
        report.append("")
        report.append(f"**数据期间**: {data[0]['date'].strftime('%Y-%m-%d')} 至 {data[-1]['date'].strftime('%Y-%m-%d')}")
        print(f"DEBUG **数据期间**: {data[0]['date'].strftime('%Y-%m-%d')} 至 {data[-1]['date'].strftime('%Y-%m-%d')}")
        report.append("")
        report.append(f"**交易日数**: {len(data)}天")
        report.append("")
        report.append(f"**上市首日开盘价**: {data[0]['open']:.3f}元")
        report.append("")
        report.append(f"**最新收盘价**: {data[-1]['close']:.3f}元")
        report.append("")
        total_return = (data[-1]['close'] - data[0]['open']) / data[0]['open'] * 100
        report.append(f"**累计涨跌**: {total_return:.2f}%")
        report.append("")

        if historical_analysis:
            report.append(f"**历史分析次数**: {len(historical_analysis)}次")
            report.append(f"**上次分析日期**: {historical_analysis[-1]['date']}")
            report.append("")

        # ===== 一、年度走势特点分析 =====
        report.append("---")
        report.append("")
        report.append("## 一、年度走势特点分析")
        report.append("")
        report.append("### 1.1 年度高低点统计")
        report.append("| 年份 | 年度低点 | 低点日期 | 年度高点 | 高点日期 | 年度收益率 | 年度波幅 |")
        report.append("|------|---------|----------|---------|----------|-----------|---------|")
        for s in stats:
            report.append(f"| {s['year']} | {s['low']:.3f} | {s['low_date']} | {s['high']:.3f} | {s['high_date']} | {s['return']:.2f}% | {s['range']:.2f}% |")
        
        # 生成并嵌入年度收益率走势图
        if chart_generator:
            chart_path = chart_generator.generate_annual_return_chart(stats)
            if chart_path:
                report.append("")
                report.append("### 年度收益率走势图")
                report.append("")
                report.append(f"![年度收益率走势图]({chart_path.replace(path_replaced, "")[1:]})")
                report.append("")

        # 生成并嵌入年度高低点走势图
        if chart_generator:
            chart_path = chart_generator.generate_annual_high_low_chart(stats)
            if chart_path:
                report.append("")
                report.append("### 年度高低点走势图")
                report.append("")
                report.append(f"![年度高低点走势图]({chart_path.replace(path_replaced, "")[1:]})")
                report.append("")

        report.append("### 1.2 走势特点总结")
        report.append("")
        avg_return = sum(s['return'] for s in stats) / len(stats)
        avg_range = sum(s['range'] for s in stats) / len(stats)
        report.append(f"1. **长期表现**: 近{len(stats)}年平均年化收益率为{avg_return:.2f}%")
        report.append("")
        report.append(f"2. **波动特征**: 年度波幅平均为{avg_range:.2f}%，具有较高的波动性")
        report.append("")
        report.append("3. **季节性规律**: 待分析具体数据")
        report.append("")
        report.append("")

        # ===== 二、当前市场建议 / 增量分析 =====
        if historical_analysis:
            report.append("---")
            report.append("")
            report.append("## 二、增量分析 (与上次分析对比)")
            report.append("")

            last_analysis = historical_analysis[-1]
            last_date = datetime.strptime(last_analysis['date'], '%Y-%m-%d')
            current_date = data[-1]['date']
            days_diff = (current_date - last_date).days
            estimated_trading_days = int(days_diff * 5 / 7)

            report.append("### 2.1 数据变化")
            report.append("")
            report.append(f"- 新增交易日数: ~{estimated_trading_days}天 (实际日期差{days_diff}天)")
            report.append("")
            report.append(f"- 价格变化: 需要从历史报告中解析，当前最新价: {data[-1]['close']:.3f}元")
            report.append("")
            if len(data) > 1:
                report.append(f"- 期间价格范围: {min(d['low'] for d in data):.3f} - {max(d['high'] for d in data):.3f}元")
                report.append("")

            report.append("### 2.2 策略调整建议")
            report.append("")
            current_price = data[-1]['close']
            avg_price = sum(d['close'] for d in data) / len(data)

            if current_price < avg_price * 0.9:
                report.append("- 当前价格显著低于期间平均价，考虑分批建仓机会")
                report.append("")
            elif current_price > avg_price * 1.1:
                report.append("- 当前价格显著高于期间平均价，注意回调风险")
                report.append("")
            else:
                report.append("- 当前价格处于期间合理区间，可考虑波段操作")
                report.append("")

            report.append("- 建议结合最新季节性规律和市场环境调整仓位")
            report.append("")
            report.append("- 关注年度低点附近的支撑位和年度高点附近的压力位")
            report.append("")
        else:
            report.append("---")
            report.append("")
            report.append("## 二、 当前市场建议")
            report.append("")
            current_price = data[-1]['close']
            all_prices = [d['close'] for d in data]
            current_percentile = sum(1 for p in all_prices if p <= current_price) / len(all_prices) * 100

            report.append(f"**当前位置**: {current_price:.3f}元")
            report.append("")
            report.append(f"**历史分位**: 第{current_percentile:.0f}百分位")
            report.append("")
            if current_percentile < 20:
                report.append("**判断**: 当前处于历史低位区域，可能存在价值洼地")
                report.append("")
            elif current_percentile > 80:
                report.append("**判断**: 当前处于历史高位区域，需注意回调风险")
                report.append("")
            else:
                report.append("**判断**: 当前处于历史中等区域，可考虑波段操作")
                report.append("")

        # ===== 三、波动规律与季节性分析 =====
        if monthly_analyzer and seasonal_analyzer:
            report.append("---")
            report.append("")
            report.append("## 三、波动规律与季节性分析")
            report.append("")

            monthly_result = monthly_analyzer.analyze_monthly_quarterly(data)
            seasonal_result = seasonal_analyzer.analyze_seasonal_patterns(data)

            if monthly_result:
                report.append("### 3.1 月度波动规律")
                report.append("")
                report.append("| 月份 | 平均价格 | 月度收益率 | 波动幅度 | 交易天数 |")
                report.append("|------|----------|------------|----------|----------|")
                # 只显示最近12个月
                for m in monthly_result['monthly'][-12:]:
                    report.append(f"| {m['month']} | {m['avg_price']:.3f} | {m['return']:.2f}% | {m['volatility']:.2f}% | {m['trading_days']} |")
                report.append("")
                
                # 生成并嵌入月度波动模式图
                if chart_generator:
                    chart_path = chart_generator.generate_monthly_volatility_chart(monthly_result['monthly'])
                    if chart_path:
                        report.append("")
                        report.append("### 月度波动模式图")
                        report.append("")
                        report.append(f"![月度波动模式图]({chart_path.replace(path_replaced, "")[1:]})")
                        report.append("")

            if seasonal_result:
                report.append("### 3.2 季节性规律")
                report.append("")
                report.append("| 平均收益率 | 月份名称 |")
                report.append("|------------|----------|")
                for s in seasonal_result:
                    report.append(f"| {s['avg_return']:.2f}% | {s['month_name']} |")
                report.append("")

                # 最佳/最差月份
                positive_months = [s for s in seasonal_result if s['avg_return'] > 0]
                negative_months = [s for s in seasonal_result if s['avg_return'] < 0]

                best_months = sorted(seasonal_result, key=lambda x: x['avg_return'], reverse=True)[:3]
                worst_months = sorted(seasonal_result, key=lambda x: x['avg_return'])[:3]

                report.append("### 3.3 最佳/最差月份")
                report.append("")
                report.append("**最佳月份（平均正收益最高）:**")
                report.append("")
                for m in best_months:
                    report.append(f"- {m['month_name']}: 平均收益率 {m['avg_return']:.2f}%")
                    report.append("")

                report.append("")
                report.append("**最差月份（平均负收益最高）:**")
                report.append("")
                for m in worst_months:
                    report.append(f"- {m['month_name']}: 平均收益率 {m['avg_return']:.2f}%")
                    report.append("")

        # ===== 四、一年持有期基准 =====
        if holding_analyzer:
            holding_result = holding_analyzer.analyze_holding_period(data, days=365)
            if holding_result:
                report.append("---")
                report.append("")
                report.append("## 四、一年持有期基准")
                report.append("")
                report.append("### 4.1 一年持有期统计")
                report.append("")
                report.append(f"- 分析周期: {holding_result['period_days']} 个交易日 (约一年)")
                report.append("")
                report.append(f"- 总统计期数: {holding_result['total_periods']} 个")
                report.append("")
                report.append(f"- 盈利期数: {holding_result['profitable_periods']} 个")
                report.append("")
                report.append(f"- 亏损期数: {holding_result['total_periods'] - holding_result['profitable_periods']} 个")
                report.append("")
                report.append(f"- 胜率: {holding_result['win_rate']:.2f}%")
                report.append("")
                report.append(f"- 平均收益率: {holding_result['avg_return']:.2f}%")
                report.append("")
                report.append(f"- 最佳单期收益: {holding_result['best_return']:.2f}%")
                report.append("")
                report.append(f"- 最差单期收益: {holding_result['worst_return']:.2f}%")
                report.append("")
                report.append(f"- 中位数收益: {holding_result['median_return']:.2f}%")
                report.append("")
                report.append("")

                report.append("### 4.2 投资建议")
                report.append("")
                if holding_result['win_rate'] >= 70:
                    report.append("- 一年持有期胜率较高，适合长期持有")
                    report.append("")
                elif holding_result['win_rate'] >= 50:
                    report.append("- 一年持有期胜率一般，建议结合波段操作")
                    report.append("")
                else:
                    report.append("- 一年持有期胜率较低，建议以波段操作为主")
                    report.append("")

                if holding_result['avg_return'] > 0:
                    report.append(f"- 长期持有预期正收益，年化约 {holding_result['avg_return']:.2f}%")
                    report.append("")
                else:
                    report.append("- 长期持有预期收益有限，需注意时机选择")
                    report.append("")

        # ===== 五、波段分析 =====
        if wave_analyzer:
            waves = wave_analyzer.analyze_waves(data)
            if waves:
                report.append("---")
                report.append("")
                report.append("## 五、波段分析")
                report.append("")
                report.append("### 5.1 波段识别统计")
                report.append("")
                report.append(f"- 识别出的转折点总数: {len(waves['pivot_points'])} 个")
                report.append("")
                report.append(f"- 完整波段数量: {waves['total_waves']} 个")
                report.append("")

                if waves['current_wave']:
                    cw = waves['current_wave']
                    required_keys = ['status', 'progress', 'current_price', 'wave_type']
                    if all(key in cw for key in required_keys):
                        report.append(f"- 当前波段状态: {cw['status']}")
                        report.append("")
                        report.append(f"- 当前波段进度: {cw['progress']:.2f}%")
                        report.append("")
                        report.append(f"- 当前价格: {cw['current_price']:.3f}元")
                        report.append("")
                        start_price_val = cw.get('start_price')
                        end_price_val = cw.get('end_price')
                        start_date_val = cw.get('start_date')
                        end_date_val = cw.get('end_date')
                        if all(v is not None for v in [start_price_val, end_price_val, start_date_val, end_date_val]):
                            if cw['wave_type'] == 'up':
                                report.append(f"- 起点价格: {start_price_val:.3f}元 ({start_date_val})")
                                report.append("")
                                report.append(f"- 终点价格: {end_price_val:.3f}元 ({end_date_val})")
                                report.append("")
                            else:
                                report.append(f"- 起点价格: {start_price_val:.3f}元 ({start_date_val})")
                                report.append("")
                                report.append(f"- 终点价格: {end_price_val:.3f}元 ({end_date_val})")
                                report.append("")
                        else:
                            report.append("- 当前波段价格信息不完整")
                            report.append("")
                    else:
                        report.append("- 当前波段信息不完整")
                        report.append("")

                report.append(f"- 当前价格距离最近高点回撤: {waves['current_drawdown']:.2f}%")
                report.append("")

                # 历史波段表现
                if waves['wave_stats']:
                    report.append("")
                    report.append("### 5.2 历史波段表现")
                    report.append("")
                    report.append("| 波段类型 | 起点日期 | 起点价格 | 终点日期 | 终点价格 | 振幅/回撤 | 持续天数 |")
                    report.append("|----------|----------|----------|----------|----------|-----------|----------|")
                    # 显示后6个波段数据（最近的6个波段）
                    recent_waves = waves['wave_stats'][-6:] if len(waves['wave_stats']) >= 6 else waves['wave_stats']
                    for w in recent_waves:
                        # 将波段类型转换为中文显示
                        wave_type_cn = '上升' if w['wave_type'] == 'up' else '下降'
                        report.append(f"| {wave_type_cn} | {w['start_date']} | {w['start_price']:.3f} | {w['end_date']} | {w['end_price']:.3f} | {w['amplitude']:.2f}% | {w['duration_days']} |")
                    report.append("")
                print(f"DEBUG: About to process wave trend chart section")
                if chart_generator:
                    # Filter recent waves and data by recent_waves time range >= 180 days
                    cutoff_date = datetime.strptime(recent_waves[0]['start_date'], '%Y-%m-%d')
                    if (data[-1]['date'] - cutoff_date).days < 180 :
                        cutoff_date = data[-1]['date'] - timedelta(days=180)
                    # Filter data (net value time series)
                    filtered_data = [d for d in data if d['date'] >= cutoff_date]
                    print(f"DEBUG: filtered_data start_date is {cutoff_date} {filtered_data[0]['date']} end_date is {filtered_data[-1]['date']}")
                    # Create filtered waves dict
                    filtered_waves = waves.copy()
                    filtered_waves['pivot_points'] = [p for p in waves.get('pivot_points', []) if p['date'] >= cutoff_date and p['date'] <= data[-1]['date']] 
                    # Optionally update total_waves to reflect filtered count
                    filtered_waves['total_waves'] = len(filtered_waves['pivot_points'])
                    filtered_waves['wave_stats'] = recent_waves
                    chart_path = chart_generator.generate_wave_trend_chart(filtered_data, filtered_waves)
                    if chart_path:
                        report.append("")
                        report.append("### 波段走势图")
                        report.append("")
                        report.append(f"![波段走势图]({chart_path.replace(path_replaced, '')[1:]})")
                        print(f"DEBUG: Report length before adding chart: {len(report)}")
                        report.append("")

                # 波段分析结论
                report.append("### 5.3 波段分析结论")
                report.append("")
                # 波段分析结论
                report.append("### 5.3 波段分析结论")
                report.append("")
                if waves['current_wave']:
                    cw = waves['current_wave']
                    if cw.get('wave_type') == 'up':
                        report.append("- 当前处于上升波段中，趋势向好")
                        report.append("")
                        if cw.get('progress', 0) < 30:
                            report.append("- 波段处于初期，可考虑加仓")
                            report.append("")
                        elif cw.get('progress', 0) < 70:
                            report.append("- 波段处于中期，可考虑短线操作")
                            report.append("")
                        else:
                            report.append("- 波段处于后期，注意止盈")
                            report.append("")
                    else:
                        report.append("- 当前处于下降波段中，需防守为主")
                        report.append("")
                        if cw.get('progress', 0) < 30:
                            report.append("- 下降波段初期，建议减仓观望")
                            report.append("")
                        elif cw.get('progress', 0) < 70:
                            report.append("- 下降波段处于中期，建议观望")
                            report.append("")
                        else:
                            report.append("- 下降波段后期，可关注抄底机会")
                            report.append("")
                else:
                    report.append("- 当前无明确波段信号，建议观望")
                    report.append("")

        # ===== 六、买入时机分析 =====
        report.append("---")
        report.append("")
        report.append("## 六、买入时机分析")
        report.append("")
        report.append("### 6.1 历史低点回顾")
        report.append("| 低点日期 | 低点价格 | 距前一年高点跌幅 | 反弹幅度(3个月内) |")
        report.append("|----------|----------|------------------|------------------|")
        for s in stats[-3:]:
            low_date = s['low_date']
            low_price = s['low']
            drop_str = f"{s['drop_from_prev_high']:.2f}%" if s['drop_from_prev_high'] is not None else "N/A"
            rebound_str = f"{s['rebound_3m']:.2f}%" if s['rebound_3m'] is not None else "N/A"
            report.append(f"| {low_date} | {low_price:.3f} | {drop_str} | {rebound_str} |")
        report.append("")
        
        # 基于数据的定制化买入建议
        report.append("### 6.2 买入策略建议")
        report.append("")
        
        # 计算当前价格相对于历史高点的位置
        all_prices = [d['high'] for d in data]
        max_high = max(all_prices)
        min_low = min([d['low'] for d in data])
        current_price = data[-1]['close']
        
        if current_price < min_low * 1.05:
            report.append("**当前位置**：处于历史相对低位区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 估值具备一定吸引力，可考虑分批建仓策略")
            report.append("- 建议采用金字塔式建仓：首次30%，后续每下跌3-5%加仓20-30%")
            report.append("- 重点关注底部形态确认信号（如MACD金叉、成交量放大）")
            report.append("")
        elif current_price > max_high * 0.9:
            report.append("**当前位置**：接近历史高位区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 估值偏高，建议谨慎追高")
            report.append("- 可等待技术性回调后寻找买入机会")
            report.append("- 若已持仓，建议考虑部分止盈，锁定收益")
            report.append("")
        else:
            report.append("**当前位置**：处于历史中等区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 可结合技术面指标择机介入")
            report.append("- 关注季度末、年底等关键时间窗口的波动机会")
            report.append("- 建议设置明确止损位，控制单笔仓位风险")
            report.append("")
        
        report.append("**左侧交易（价值投资）**：")
        report.append("")
        report.append(f"- **条件**：价格较年度高点回撤超过35%（当前回撤{((max_high - current_price) / max_high * 100):.1f}%）")
        report.append("")
        report.append(f"- **信号**：成交量萎缩、RSI低于30、MACD底背离")
        report.append("")
        report.append(f"- **时机**：确认底部形态后，在低点出现后的1-2周内分批买入")
        report.append("")
        
        report.append("**右侧交易（趋势跟随）**：")
        report.append("")
        report.append(f"- **条件**：确认底部形态（W底、头肩底）并有效突破颈线位")
        report.append("")
        report.append(f"- **信号**：连续3日收于短期均线之上、MACD金叉、成交量配合放大")
        report.append("")
        report.append(f"- **时机**：突破确认后，回踩确认支撑时加仓")
        report.append("")
        
        # 基于季节性数据的建议
        if seasonal_result:
            best_months = [m for m in seasonal_result if m['avg_return'] > 0]
            worst_months = [m for m in seasonal_result if m['avg_return'] < 0]
            
            if best_months:
                best_month_names = [m['month_name'] for m in best_months[:2]]
                report.append(f"**季节性机会**：")
                report.append(f"- 最佳买入窗口：{', '.join(best_month_names)}（平均正收益）")
                report.append(f"- 建议策略：在季节性高点前1-2个月布局，季节性低点后观察反弹机会")
                report.append("")
        
        report.append("**右侧交易（趋势跟随）**：")
        report.append("")
        report.append(f"- **条件**：确认底部形态（W底、头肩底）并有效突破颈线位")
        report.append("")
        report.append(f"- **信号**：连续3日收于短期均线之上、MACD金叉、成交量配合放大")
        report.append("")
        report.append(f"- **时机**：突破确认后，回踩确认支撑时加仓")
        report.append("")
        
        # 基于季节性数据的建议
        if seasonal_result:
            best_months = [m for m in seasonal_result if m['avg_return'] > 0]
            worst_months = [m for m in seasonal_result if m['avg_return'] < 0]
            
            if best_months:
                best_month_names = [m['month_name'] for m in best_months[:2]]
                report.append(f"**季节性机会**：")
                report.append(f"- 最佳买入窗口：{', '.join(best_month_names)}（平均正收益）")
                report.append(f"- 建议策略：在季节性高点前1-2个月布局，季节性低点后观察反弹机会")
                report.append("")
            
            if worst_months:
                worst_month_names = [m['month_name'] for m in worst_months[:2]]
                report.append(f"**季节性风险**：")
                report.append(f"- 需规避窗口：{', '.join(worst_month_names)}（平均负收益）")
                report.append(f"- 建议策略：在这些月份避免重仓买入，或考虑对冲策略")
                report.append("")

        # ===== 七、卖出时机分析 =====
        report.append("---")
        report.append("")
        report.append("## 七、卖出时机分析")
        report.append("")
        report.append("### 7.1 历史高点回顾")
        report.append("| 高点日期 | 高点价格 | 距前一年低点涨幅 | 持续天数 | 后续最大回撤 |")
        report.append("|----------|----------|------------------|----------|--------------|")
        for s in stats[-3:]:
            high_date = s['high_date']
            high_price = s['high']
            rise_str = f"{s['rise_from_prev_low']:.2f}%" if s['rise_from_prev_low'] is not None else "N/A"
            days_str = f"{s['days_low_to_high']}天" if s['days_low_to_high'] is not None else "N/A"
            drawdown_str = f"{s['max_drawdown_after_high']:.2f}%" if s['max_drawdown_after_high'] is not None else "N/A"
            report.append(f"| {high_date} | {high_price:.3f} | {rise_str} | {days_str} | {drawdown_str} |")
        report.append("")
        
        # 基于数据的定制化卖出建议
        report.append("### 7.2 卖出策略建议")
        report.append("")
        
        # 计算当前价格相对于历史低点的位置
        all_prices = [d['close'] for d in data]
        max_high = max([d['high'] for d in data])
        min_low = min([d['low'] for d in data])
        current_price = data[-1]['close']
        
        if current_price > min_low * 1.15:
            report.append("**当前位置**：处于历史相对高位区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 估值偏高，建议谨慎追高")
            report.append("- 可等待技术性回调后寻找卖出机会")
            report.append("- 若已持仓，建议考虑部分止盈，锁定收益")
            report.append("")
        elif current_price < max_high * 0.9:
            report.append("**当前位置**：接近历史低位区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 估值具备一定吸引力，建议持有或逢低加仓")
            report.append("- 若已减仓，可考虑在技术性反弹时重新建仓")
            report.append("- 避免在低位过早止损，可设置移动止损位")
            report.append("")
        else:
            report.append("**当前位置**：处于历史中等区域")
            report.append("")
            report.append("**专业建议**：")
            report.append("- 可结合技术面指标择机操作")
            report.append("- 建议设置明确止盈目标，避免贪婪")
            report.append("- 关注年度低点附近的支撑位和年度高点附近的压力位")
            report.append("")
        
        report.append("**目标收益率止盈**：")
        report.append("")
        
        # 基于历史平均收益设置目标
        if holding_analyzer and holding_result:
            avg_return = holding_result['avg_return']
            median_return = holding_result['median_return']
            
            report.append(f"- **保守目标**：{median_return:.1f}%（接近历史中位数）")
            report.append(f"- **中性目标**：{avg_return + median_return:.1f}%（历史平均+中位数）")
            report.append(f"- **乐观目标**：{avg_return + median_return * 2:.1f}%（历史平均+2倍中位数）")
            report.append("")
            report.append(f"- **说明**：基于历史数据，超过此收益率的概率约50%，需结合市场环境调整")
            report.append("")
        
        report.append("**技术止盈信号**：")
        report.append("")
        report.append("- **顶部形态**：双顶、三重顶、头肩顶")
        report.append("- **量价背离**：价格新高但成交量萎缩（RSI高于70时尤其明显）")
        report.append("- **均线死叉**：短期均线下穿长期均线，且持续3日以上")
        report.append("- **MACD顶背离**：价格创新高但MACD指标未创新高")
        report.append("")
        report.append("**时间止盈策略**：")
        report.append("")
        report.append("- **单笔持仓周期**：建议不超过6个月，避免长期持有导致时间成本上升")
        report.append("- **季度评估**：每季度末评估基金表现，偏离目标价±10%时考虑调仓")
        report.append("- **年度再平衡**：每年底重新评估投资组合，根据市场环境调整仓位")
        report.append("")
        
        # 基于历史最大回撤设置止损位
        max_drawdown = max([s['max_drawdown_after_high'] for s in stats] if stats else [0])
        report.append("**风险控制**：")
        report.append("")
        report.append(f"- **最大回撤参考**：历史高点后最大回撤{max_drawdown:.1f}%")
        report.append("- **建议止损位**：从高点回撤{max_drawdown * 0.6:.1f}%时考虑止损")
        report.append("- **移动止盈**：最高点回撤10%时止盈，锁定大部分收益")
        report.append("")

        # ===== 八、预估收益率 =====
        report.append("---")
        report.append("")
        report.append("## 八、预估收益率")
        report.append("")
        report.append("### 8.1 基于历史数据的统计")
        report.append("| 情景 | 年化收益率 | 概率 | 说明 |")
        report.append("|------|-----------|------|------|")
        
        # 基于历史数据计算概率
        if holding_analyzer and holding_result:
            avg_return = holding_result['avg_return']
            win_rate = holding_result['win_rate']
            median_return = holding_result['median_return']
            best_return = holding_result['best_return']
            worst_return = holding_result['worst_return']
            
            # 保守情景：低于中位数-1倍标准差
            conservative_return = median_return * 0.8
            conservative_prob = max(20, min(50, 100 - win_rate))  # 胜率越低，保守概率越高
            
            # 中性情景：历史平均收益率
            neutral_return = avg_return
            neutral_prob = 35
            
            # 乐观情景：高于中位数+1倍标准差
            optimistic_return = median_return * 1.2
            optimistic_prob = max(10, min(50, win_rate))  # 胜率越高，乐观概率越高
            
            # 极端乐观情景：最佳收益率
            extreme_optimistic_return = best_return
            extreme_optimistic_prob = 5
            
            report.append(f"| 保守 | {conservative_return:.1f}% 至 {conservative_return + 5:.1f}% | {conservative_prob:.0f}% | 行业继续探底或市场低迷，历史中位数以下表现 |")
            report.append(f"| 中性 | {neutral_return:.1f}% 至 {neutral_return + 5:.1f}% | {neutral_prob:.0f}% | 行业筑底或震荡，政策托底但无强刺激 |")
            report.append(f"| 乐观 | {optimistic_return:.1f}% 至 {optimistic_return + 10:.1f}% | {optimistic_prob:.0f}% | 政策强力刺激，类似历史反弹行情 |")
            report.append(f"| 极端乐观 | {extreme_optimistic_return:.1f}%+ | {extreme_optimistic_prob:.0f}% | 行业基本面反转，类似历史最佳表现 |")
        else:
            report.append(f"| 保守 | -15% 至 -5% | 40% | 行业继续探底，无重大政策利好 |")
            report.append(f"| 中性 | 0% 至 +15% | 35% | 行业筑底，政策托底但无强刺激 |")
            report.append(f"| 乐观 | +20% 至 +40% | 20% | 政策强力刺激，类似历史反弹行情 |")
            report.append(f"| 极端乐观 | +50%+ | 5% | 行业基本面反转 |")
        
        report.append("")
        report.append("### 8.2 风险提示")
        report.append("")
        report.append(f"- **最大回撤风险**：历史最大回撤约{max_drawdown:.1f}%，需做好仓位管理")
        report.append(f"- **波动率风险**：年度波幅平均{avg_range:.1f}%，波动较大")
        report.append(f"- **胜率风险**：一年持有期胜率{win_rate:.1f}%，需注意时机选择")
        report.append("")

        # ===== 九、投资策略建议 =====
        report.append("---")
        report.append("")
        report.append("## 九、投资策略建议")
        report.append("")
        report.append("### 9.1 三种操作方案")
        report.append("")
        report.append("#### 方案一：保守型（低风险偏好）")
        report.append("")
        report.append("- 建仓：当前价位30%，回调至前低附近加仓")
        report.append("")
        report.append("- 止盈：目标收益率20-33%")
        report.append("")
        report.append("- 止损：跌破前低全部止损")
        report.append("")
        report.append("- 适合人群：风险厌恶型投资者、退休资金")
        report.append("")
        report.append("- 预期年化：8%-15%")
        report.append("")
        report.append("")
        report.append("#### 方案二：平衡型（中等风险偏好）")
        report.append("")
        report.append("- 建仓：当前价位40%，每下跌3%加仓10%，最多加仓至80%")
        report.append("")
        report.append("- 止盈：每上涨10%减仓20%，目标收益率30-40%")
        report.append("")
        report.append("- 止损：跌破前低止损50%，跌破更低前低清仓")
        report.append("")
        report.append("- 适合人群：稳健型投资者、希望获得中等收益的投资者")
        report.append("")
        report.append("- 预期年化：15%-25%")
        report.append("")
        report.append("")
        report.append("#### 方案三：激进型（高风险偏好）")
        report.append("")
        report.append("- 建仓：当前价位一次性建仓70%，保留30%资金补仓")
        report.append("")
        report.append("- 止盈：目标收益率50%+，采用移动止盈（最高点回撤10%止盈）")
        report.append("")
        report.append("- 止损：亏损15%无条件离场")
        report.append("")
        report.append("- 适合人群：风险偏好型投资者、追求高收益的投资者")
        report.append("")
        report.append("- 预期年化：25%-40%")
        report.append("")

        # ===== 十、风险管理 =====
        report.append("---")
        report.append("")
        report.append("## 十、风险管理")
        report.append("")
        
        # 基于历史数据的风险管理建议
        if holding_analyzer and holding_result:
            win_rate = holding_result['win_rate']
            avg_return = holding_result['avg_return']
            median_return = holding_result['median_return']
            max_drawdown = max([s['max_drawdown_after_high'] for s in stats] if stats else [0])
            avg_range = sum(s['range'] for s in stats) / len(stats) if stats else 0
            
            report.append(f"- **仓位控制**：考虑到波动率{avg_range:.1f}%，建议单只基金仓位不超过总资产的{max(15, 30 - avg_range/5):.0f}%")
            report.append("")
            report.append(f"- **单笔最大亏损**：建议不超过总资金的{max(1, 2 - avg_range/10):.0f}%，避免单一投资导致过大回撤")
            report.append("")
            report.append(f"- **持仓时间**：基于{win_rate:.1f}%的胜率，建议单笔持仓不超过6个月，避免长期持有导致收益被时间成本侵蚀")
            report.append("")
            report.append(f"- **再评估周期**：超过{max(2, 3 - avg_range/10):.0f}个月未达目标需重新评估，避免陷入长期亏损")
            report.append("")
            report.append(f"- **止损纪律**：严格执行止损，胜率{win_rate:.1f}%意味着{100-win_rate:.0f}%的时间可能亏损，必须控制单笔损失")
            report.append("")
            report.append(f"- **分散投资**：建议将{max(2, 4 - avg_range/5):.0f}只不同类型的基金组合投资，降低单一基金波动风险")
        else:
            report.append("- 仓位控制：行业ETF占总资产不超过20%")
            report.append("")
            report.append("- 单笔最大亏损：不超过总资金的2%")
            report.append("")
            report.append("- 持仓时间：不超过6个月")
            report.append("")
            report.append("- 再评估周期：超过3个月未达目标需重新评估")
            report.append("")
            report.append("- 止损纪律：严格执行止损，不扛单")
            report.append("")
            report.append("- 分散投资：建议将不同类型的基金组合投资")
            report.append("")

        # ===== 十一、关键时间节点提醒 =====
        report.append("---")
        report.append("")
        report.append("## 十一、关键时间节点提醒")
        report.append("")
        report.append("| 时间窗口 | 操作建议 |")
        report.append("|----------|----------|")
        
        # 基于季节性数据调整时间节点建议
        if seasonal_result:
            best_months = [m for m in seasonal_result if m['avg_return'] > 0]
            worst_months = [m for m in seasonal_result if m['avg_return'] < 0]
            
            if best_months:
                best_month_names = [m['month_name'] for m in best_months[:2]]
                report.append(f"| {best_month_names[0]} | 重点关注建仓机会，避免在{best_month_names[1]}过度追高 |")
                report.append(f"| {best_month_names[1]} | 建议逐步减仓，锁定前期收益 |")
            
            if worst_months:
                worst_month_names = [m['month_name'] for m in worst_months[:2]]
                report.append(f"| {worst_month_names[0]} | 建议减仓或观望，规避风险 |")
                report.append(f"| {worst_month_names[1]} | 避免重仓建仓，可考虑对冲策略 |")
        else:
            report.append("| 每月末 | 检查基金净值表现，评估是否需要调整仓位 |")
            report.append("| 每季度末 | 重新评估投资策略，考虑是否需要再平衡 |")
            report.append("| 半年度 | 详细分析基金持仓变化和基金经理报告 |")
            report.append("| 年末 | 年度总结，制定下一年投资计划 |")
        
        report.append("")
        
        # 基于历史数据添加技术分析提醒
        if wave_analyzer and wave_analyzer.analyze_waves(data):
            waves = wave_analyzer.analyze_waves(data)
            if waves['current_wave']:
                current_wave = waves['current_wave']
                if current_wave.get('wave_type') == 'down':
                    report.append("### 技术提醒：")
                    report.append(f"- **当前趋势**：下降波段中，建议关注{current_wave.get('progress', 0):.1f}%的进度")
                    report.append("- **关键支撑位**：关注历史低点附近的技术支撑")
                    report.append("- **反弹机会**：当RSI低于30时可考虑分批建仓")
                else:
                    report.append("### 技术提醒：")
                    report.append(f"- **当前趋势**：上升波段中，建议关注{current_wave.get('progress', 0):.1f}%的进度")
                    report.append("- **关键压力位**：关注历史高点附近的技术压力")
                    report.append("- **止盈机会**：当RSI高于70时可考虑分批止盈")
        else:
            report.append("### 技术提醒：")
            report.append("- 每月末关注MACD、RSI等技术指标的变化")
            report.append("- 每季度末关注均线系统的交叉情况")
            report.append("- 半年度关注成交量与价格的关系")
        report.append("")

        # ===== 十二、综合建议 =====
        report.append("---")
        report.append("")
        report.append("## 十二、综合建议")
        report.append("")
        
        # 基于历史数据生成综合建议
        if holding_analyzer and holding_result:
            win_rate = holding_result['win_rate']
            avg_return = holding_result['avg_return']
            median_return = holding_result['median_return']
            max_drawdown = max([s['max_drawdown_after_high'] for s in stats] if stats else [0])
            
            # 根据胜率和建议策略
            if win_rate >= 60 and avg_return > 0:
                report.append("> **当前最优策略**：建议长期持有，分批建仓，设定明确止盈目标")
                report.append("")
                report.append("> **核心逻辑**：")
                report.append(f"1. 胜率{win_rate:.1f}%较高，平均年化收益{avg_return:.1f}%，适合长期投资")
                report.append(f"2. 最大回撤{max_drawdown:.1f}%，可通过仓位管理控制在可承受范围内")
                report.append('3. 建议采用“核心+卫星”策略，核心仓位长期持有，卫星仓位波段操作')
                report.append("")
            elif win_rate >= 40:
                report.append("> **当前最优策略**：建议波段操作为主，控制单笔仓位，设置严格止损")
                report.append("")
                report.append("> **核心逻辑**：")
                report.append(f"1. 胜率{win_rate:.1f}%一般，不适合长期持有，建议以波段操作为主")
                report.append(f"2. 平均收益{avg_return:.1f}%，需通过波段操作提升收益")
                report.append(f"3. 最大回撤{max_drawdown:.1f}%，建议单笔仓位不超过20%")
                report.append("")
            else:
                report.append("> **当前最优策略**：建议观望为主，等待更好的买入时机")
                report.append("")
                report.append("> **核心逻辑**：")
                report.append(f"1. 胜率{win_rate:.1f}%较低，长期持有可能持续亏损")
                report.append(f"2. 建议关注历史低点附近的买入机会，避免在高位追涨")
                report.append("")
            
            report.append("> **需要关注的风险信号**：")
            report.append("")
            report.append(f"- **年度波动风险**：年度波幅平均{avg_range:.1f}%，建议设置{max(15, 30 - avg_range/2):.0f}%的止损位")
            report.append(f"- **回撤控制**：历史最大回撤{max_drawdown:.1f}%，需做好仓位管理")
            report.append("- **流动性风险**：关注基金规模变化，避免在规模急剧缩小时被强制赎回")
            report.append("")
        else:
            report.append("> **当前最优策略**：根据当前市场情况选择合适的操作方案")
            report.append("")
            report.append("> **核心逻辑**：")
            report.append("")
            report.append("1. 结合基本面分析和技术面指标进行综合判断")
            report.append("")
            report.append("2. 严格控制风险，设定明确的止盈止损点")
            report.append("")
            report.append("3. 根据市场环境灵活调整投资策略")
            report.append("")
            report.append("> **需要关注的风险信号**：")
            report.append("")
            report.append("- 基金规模急剧缩小")
            report.append("")
            report.append("- 基金经理频繁更换")
            report.append("")
            report.append("- 行业政策出现重大不利变化")
            report.append("")

        # ===== 免责声明 =====
        report.append("---")
        report.append("")
        report.append("## 免责声明")
        report.append("")
        report.append("")
        report.append("本分析仅基于历史数据，不构成投资建议。市场有风险，投资需谨慎。")
        report.append("")
        report.append("历史表现不代表未来结果，请根据自身风险承受能力谨慎决策。")

        return "\n".join(report)
