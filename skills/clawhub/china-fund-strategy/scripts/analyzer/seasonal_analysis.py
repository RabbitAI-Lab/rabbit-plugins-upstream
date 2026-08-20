"""
Seasonal Analyzer Module

Handles seasonal pattern analysis across years.
"""

from typing import List, Dict, Any
from datetime import datetime
from collections import defaultdict


class SeasonalAnalyzer:
    def analyze_seasonal_patterns(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform seasonal pattern analysis.
        
        Args:
            data: List of fund data records with date, open, close, high, low, volume
            
        Returns:
            Dictionary containing monthly average returns across years
        """
        if len(data) < 30:
            return None
        
        # Group by month across all years
        monthly_returns = defaultdict(list)
        
        for row in data:
            month = row['date'].month  # 1-12
            # Calculate monthly return if we have enough data
            # For simplicity, we'll calculate return from first to last day of month
            # But since we don't have grouped by month within year easily, 
            # we'll use a different approach: calculate daily returns and aggregate by month
            
            # Actually, for seasonal analysis, we want to see average performance for each month
            # across different years. We need to calculate monthly returns first.
            pass
        
        # Simplified approach: calculate average return for each calendar month
        # by grouping all data points by month and calculating average daily return
        # then compounding approximately
        
        daily_returns_by_month = defaultdict(list)
        
        # Sort data by date
        sorted_data = sorted(data, key=lambda x: x['date'])
        
        # Calculate daily returns
        for i in range(1, len(sorted_data)):
            prev_close = sorted_data[i-1]['close']
            curr_close = sorted_data[i]['close']
            if prev_close != 0:
                daily_return = (curr_close - prev_close) / prev_close
                month = sorted_data[i]['date'].month
                daily_returns_by_month[month].append(daily_return)
        
        # Calculate average monthly return (approximate)
        seasonal_stats = []
        month_names = ['1月', '2月', '3月', '4月', '5月', '6月',
                      '7月', '8月', '9月', '10月', '11月', '12月']
        
        for month_num in range(1, 13):
            returns = daily_returns_by_month.get(month_num, [])
            if returns:
                # Simple average of daily returns (not compounded)
                avg_daily_return = sum(returns) / len(returns)
                # Approximate monthly return (21 trading days)
                monthly_return = avg_daily_return * 21 * 100  # as percentage
            else:
                monthly_return = 0
            
            seasonal_stats.append({
                'month': month_num,
                'month_name': month_names[month_num-1],
                'avg_return': monthly_return,
                'sample_size': len(returns)
            })
        
        return seasonal_stats