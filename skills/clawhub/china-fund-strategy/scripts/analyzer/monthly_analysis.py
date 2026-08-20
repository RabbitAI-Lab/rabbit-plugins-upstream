"""
Monthly Analyzer Module

Handles monthly and quarterly volatility analysis.
"""

from typing import List, Dict, Any
from datetime import datetime
from collections import defaultdict


class MonthlyAnalyzer:
    def analyze_monthly_quarterly(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform monthly and quarterly volatility analysis.
        
        Args:
            data: List of fund data records with date, open, close, high, low, volume
            
        Returns:
            Dictionary containing monthly stats, quarterly stats, best/worst months
        """
        if len(data) < 30:
            return None
        
        # Group by month and quarter
        monthly = defaultdict(list)
        quarterly = defaultdict(list)
        
        for row in data:
            month_key = row['date'].strftime('%Y-%m')
            quarter_key = f"{row['date'].year}-Q{((row['date'].month-1)//3)+1}"
            
            monthly[month_key].append(row)
            quarterly[quarter_key].append(row)
        
        # Calculate monthly statistics
        monthly_stats = []
        for month, month_data in sorted(monthly.items()):
            month_prices = [d['close'] for d in month_data]
            avg_price = sum(month_prices) / len(month_prices)
            volatility = (max(month_prices) - min(month_prices)) / avg_price * 100
            return_pct = (month_prices[-1] - month_prices[0]) / month_prices[0] * 100
            
            monthly_stats.append({
                'month': month,
                'avg_price': avg_price,
                'volatility': volatility,
                'return': return_pct,
                'trading_days': len(month_data)
            })
        
        # Calculate quarterly statistics
        quarterly_stats = []
        for quarter, quarter_data in sorted(quarterly.items()):
            quarter_prices = [d['close'] for d in quarter_data]
            avg_price = sum(quarter_prices) / len(quarter_prices)
            volatility = (max(quarter_prices) - min(quarter_prices)) / avg_price * 100
            return_pct = (quarter_prices[-1] - quarter_prices[0]) / quarter_prices[0] * 100
            
            quarterly_stats.append({
                'quarter': quarter,
                'avg_price': avg_price,
                'volatility': volatility,
                'return': return_pct,
                'trading_days': len(quarter_data)
            })
        
        # Identify best/worst months
        best_months = sorted(monthly_stats, key=lambda x: x['return'], reverse=True)[:3]
        worst_months = sorted(monthly_stats, key=lambda x: x['return'])[:3]
        
        return {
            'monthly': monthly_stats,
            'quarterly': quarterly_stats,
            'best_months': best_months,
            'worst_months': worst_months
        }