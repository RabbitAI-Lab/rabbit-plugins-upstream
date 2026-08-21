"""
Annual Analyzer Module

Handles yearly analysis of fund data including:
- Yearly high/low points
- Yearly returns and volatility
- Additional metrics like rebound potential, drawdowns, etc.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any


class AnnualAnalyzer:
    def analyze_annual(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Perform annual analysis on fund data.
        
        Args:
            data: List of fund data records with date, open, close, high, low, volume
            
        Returns:
            List of dictionaries containing annual statistics
        """
        years = {}
        for row in data:
            y = row['date'].year
            if y not in years:
                years[y] = []
            years[y].append(row)

        stats = []
        sorted_years = sorted(years.keys())
        for idx, y in enumerate(sorted_years):
            y_data = years[y]
            high_row = max(y_data, key=lambda x: x['high'])
            low_row = min(y_data, key=lambda x: x['low'])

            start_price = y_data[0]['open']
            end_price = y_data[-1]['close']
            y_return = (end_price - start_price) / start_price * 100
            price_range = (high_row['high'] - low_row['low']) / low_row['low'] * 100

            # Initialize additional fields
            drop_from_prev_high = None  # Distance from previous year's high point (for low)
            rebound_3m = None           # Rebound potential (3-month window after low) (for low)
            rise_from_prev_low = None   # Distance from previous year's low point (for high)
            days_low_to_high = None     # Days from low to high within same year
            max_drawdown_after_high = None  # Maximum drawdown after high point

            # Calculate previous year high and low (if exists)
            if idx > 0:
                prev_year = sorted_years[idx-1]
                prev_data = years[prev_year]
                prev_high = max(prev_data, key=lambda x: x['high'])['high']
                prev_low = min(prev_data, key=lambda x: x['low'])['low']
                # Distance from previous year's high point: (this year's low - previous year's high) / previous year's high * 100
                drop_from_prev_high = (low_row['low'] - prev_high) / prev_high * 100
                # Distance from previous year's low point: (this year's high - previous year's low) / previous year's low * 100
                rise_from_prev_low = (high_row['high'] - prev_low) / prev_low * 100

            # Rebound potential (3-month): highest price within 90 days after low point
            low_date = low_row['date']
            window_end = low_date + timedelta(days=90)
            rebound_candidates = [row for row in data if low_date <= row['date'] <= window_end]
            if rebound_candidates:
                max_price_in_window = max(row['high'] for row in rebound_candidates)
                rebound_3m = (max_price_in_window - low_row['low']) / low_row['low'] * 100

            # Days from low to high (within same year)
            days_low_to_high = (high_row['date'] - low_date).days

            # Maximum drawdown after high: lowest price after the high point until data ends
            high_date = high_row['date']
            drawdown_candidates = [row for row in data if row['date'] >= high_date]
            if drawdown_candidates:
                min_price_after = min(row['low'] for row in drawdown_candidates)
                # Drawdown is typically expressed as a positive percentage
                max_drawdown_after_high = abs((min_price_after - high_row['high']) / high_row['high'] * 100)

            stats.append({
                'year': y,
                'low': low_row['low'],
                'low_date': low_row['date'].strftime('%Y-%m-%d'),
                'high': high_row['high'],
                'high_date': high_row['date'].strftime('%Y-%m-%d'),
                'return': y_return,
                'range': price_range,
                'trading_days': len(y_data),
                # Additional fields
                'drop_from_prev_high': drop_from_prev_high,
                'rebound_3m': rebound_3m,
                'rise_from_prev_low': rise_from_prev_low,
                'days_low_to_high': days_low_to_high,
                'max_drawdown_after_high': max_drawdown_after_high
            })
        return stats