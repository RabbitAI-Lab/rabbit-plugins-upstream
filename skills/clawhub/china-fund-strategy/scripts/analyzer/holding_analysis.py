"""
Holding Period Analyzer Module

Analyzes holding period performance for various time frames.
"""

from typing import List, Dict, Any
from datetime import datetime, timedelta


class HoldingAnalyzer:
    def analyze_holding_period(self, data: List[Dict[str, Any]], days: int = 365) -> Dict[str, Any]:
        """
        Analyze holding period performance.
        
        Args:
            data: List of fund data records with date, open, close, high, low, volume
            days: Holding period in days (default 365 for one year)
            
        Returns:
            Dictionary containing holding period statistics
        """
        if len(data) < 2:
            return None
        
        # Sort data by date (should already be sorted, but just in case)
        sorted_data = sorted(data, key=lambda x: x['date'])
        
        total_periods = 0
        profitable_periods = 0
        returns = []
        
        # Use sliding window approach
        for i in range(len(sorted_data) - days + 1):
            start_data = sorted_data[i]
            end_data = sorted_data[i + days - 1]
            
            start_price = start_data['close']
            end_price = end_data['close']
            
            if start_price != 0:
                period_return = (end_price - start_price) / start_price * 100
                returns.append(period_return)
                total_periods += 1
                
                if period_return > 0:
                    profitable_periods += 1
        
        if total_periods == 0:
            return None
        
        win_rate = (profitable_periods / total_periods) * 100
        avg_return = sum(returns) / len(returns) if returns else 0
        best_return = max(returns) if returns else 0
        worst_return = min(returns) if returns else 0
        
        # Calculate median return
        sorted_returns = sorted(returns)
        n = len(sorted_returns)
        if n % 2 == 0:
            median_return = (sorted_returns[n//2-1] + sorted_returns[n//2]) / 2
        else:
            median_return = sorted_returns[n//2]
        
        return {
            'period_days': days,
            'total_periods': total_periods,
            'profitable_periods': profitable_periods,
            'win_rate': win_rate,
            'avg_return': avg_return,
            'best_return': best_return,
            'worst_return': worst_return,
            'median_return': median_return,
            'returns': returns  # For potential further analysis
        }