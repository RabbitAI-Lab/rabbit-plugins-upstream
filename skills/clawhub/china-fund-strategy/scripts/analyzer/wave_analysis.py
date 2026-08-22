"""
Wave Analyzer Module

Implements ZigZag algorithm for identifying pivot points and wave patterns
in financial time series data.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime


class WaveAnalyzer:
    def analyze_waves(self, data: List[Dict[str, Any]], deviation: float = 5.0) -> Dict[str, Any]:
        """
        Perform ZigZag wave analysis on fund data.
        
        Args:
            data: List of fund data records with date, open, close, high, low, volume
            deviation: Minimum percentage change to form a new zigzag point (default 5.0%)
            
        Returns:
            Dictionary containing pivot points, wave statistics, current wave info, and drawdown
        """
        if len(data) < 2:
            return None
        
        # Step 1: Identify pivot points using ZigZag algorithm
        pivot_highs, pivot_lows = self._find_pivot_points(data, deviation)
        
        # Step 2: Combine and sort all pivot points by index
        all_points = sorted(pivot_highs + pivot_lows, key=lambda x: x['index'])
        
        # Step 3: Build waves from alternating high-low points
        waves = self._build_waves(all_points)
        
        # Step 4: Calculate wave statistics
        wave_stats = self._calculate_wave_statistics(waves)
        
        # Step 5: Determine current wave status
        current_wave_info = self._get_current_wave_info(data, waves)
        
        # Step 6: Calculate current drawdown from recent high
        current_drawdown = self._calculate_current_drawdown(data)
        
        return {
            'pivot_points': all_points,
            'wave_stats': wave_stats,
            'current_wave': current_wave_info,
            'current_drawdown': current_drawdown,
            'total_waves': len(wave_stats)
        }
    
    def _find_pivot_points(self, data: List[Dict[str, Any]], deviation: float) -> tuple:
        """Find pivot highs and lows using ZigZag algorithm."""
        pivot_highs = []
        pivot_lows = []
        
        if len(data) < 2:
            return pivot_highs, pivot_lows
        
        # Start with first point as both potential high and low
        last_pivot_index = 0
        last_pivot_price = data[0]['close']
        last_pivot_type = None  # None, 'high', or 'low'
        
        # Look for the first confirmed pivot
        for i in range(1, len(data)):
            current_price = data[i]['close']
            price_change_pct = (current_price - last_pivot_price) / last_pivot_price * 100
            
            # If we haven't established a trend yet
            if last_pivot_type is None:
                if price_change_pct >= deviation:
                    # Upward movement
                    last_pivot_type = 'up'
                    # The previous point is a pivot low
                    pivot_lows.append({
                        'index': last_pivot_index,
                        'date': data[last_pivot_index]['date'],
                        'price': last_pivot_price,
                        'type': 'low'
                    })
                    last_pivot_index = i
                    last_pivot_price = current_price
                elif price_change_pct <= -deviation:
                    # Downward movement
                    last_pivot_type = 'down'
                    # The previous point is a pivot high
                    pivot_highs.append({
                        'index': last_pivot_index,
                        'date': data[last_pivot_index]['date'],
                        'price': last_pivot_price,
                        'type': 'high'
                    })
                    last_pivot_index = i
                    last_pivot_price = current_price
            # If we're in an uptrend, look for higher highs or trend reversal
            elif last_pivot_type == 'up':
                if current_price > last_pivot_price:
                    # New higher high, update the pivot
                    last_pivot_index = i
                    last_pivot_price = current_price
                elif price_change_pct <= -deviation:
                    # Trend reversal to down
                    # The previous point is a pivot high
                    pivot_highs.append({
                        'index': last_pivot_index,
                        'date': data[last_pivot_index]['date'],
                        'price': last_pivot_price,
                        'type': 'high'
                    })
                    last_pivot_type = 'down'
                    last_pivot_index = i
                    last_pivot_price = current_price
            # If we're in a downtrend, look for lower lows or trend reversal
            elif last_pivot_type == 'down':
                if current_price < last_pivot_price:
                    # New lower low, update the pivot
                    last_pivot_index = i
                    last_pivot_price = current_price
                elif price_change_pct >= deviation:
                    # Trend reversal to up
                    # The previous point is a pivot low
                    pivot_lows.append({
                        'index': last_pivot_index,
                        'date': data[last_pivot_index]['date'],
                        'price': last_pivot_price,
                        'type': 'low'
                    })
                    last_pivot_type = 'up'
                    last_pivot_index = i
                    last_pivot_price = current_price
        
        # Add the last pivot point
        if last_pivot_type == 'up':
            pivot_lows.append({
                'index': last_pivot_index,
                'date': data[last_pivot_index]['date'],
                'price': last_pivot_price,
                'type': 'low'
            })
        elif last_pivot_type == 'down':
            pivot_highs.append({
                'index': last_pivot_index,
                'date': data[last_pivot_index]['date'],
                'price': last_pivot_price,
                'type': 'high'
            })
        
        return pivot_highs, pivot_lows
    
    def _build_waves(self, all_points: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Build waves from alternating pivot points."""
        waves = []
        
        if len(all_points) < 2:
            return waves
        
        # Start with first point
        current_wave = {
            'start_index': all_points[0]['index'],
            'start_date': all_points[0]['date'],
            'start_price': all_points[0]['price'],
            'type': all_points[0]['type'],
            'end_index': all_points[0]['index'],
            'end_date': all_points[0]['date'],
            'end_price': all_points[0]['price'],
            'wave_type': 'initial'
        }
        
        # Process remaining points
        for point in all_points[1:]:
            if point['type'] != current_wave['type']:
                # Found alternating point, complete the current wave
                current_wave['end_index'] = point['index']
                current_wave['end_date'] = point['date']
                current_wave['end_price'] = point['price']
                
                # Determine wave type based on start and end types
                if current_wave['type'] == 'low' and point['type'] == 'high':
                    current_wave['wave_type'] = 'up'
                elif current_wave['type'] == 'high' and point['type'] == 'low':
                    current_wave['wave_type'] = 'down'
                else:
                    # Should not happen with proper alternation
                    current_wave['wave_type'] = 'unknown'
                
                waves.append(current_wave.copy())
                
                # Start new wave
                current_wave = {
                    'start_index': point['index'],
                    'start_date': point['date'],
                    'start_price': point['price'],
                    'type': point['type'],
                    'end_index': point['index'],
                    'end_date': point['date'],
                    'end_price': point['price'],
                    'wave_type': 'initial'
                }
            else:
                # Same type, update the end point (more extreme)
                if point['type'] == 'high' and point['price'] > current_wave['end_price']:
                    current_wave['end_index'] = point['index']
                    current_wave['end_date'] = point['date']
                    current_wave['end_price'] = point['price']
                elif point['type'] == 'low' and point['price'] < current_wave['end_price']:
                    current_wave['end_index'] = point['index']
                    current_wave['end_date'] = point['date']
                    current_wave['end_price'] = point['price']
        
        return waves
    
    def _calculate_wave_statistics(self, waves: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Calculate statistics for each completed wave."""
        wave_stats = []
        
        for wave in waves:
            if wave['wave_type'] == 'initial':
                continue  # Skip incomplete waves
            
            # Calculate amplitude (absolute percentage change)
            if wave['wave_type'] == 'up':
                amplitude = (wave['end_price'] - wave['start_price']) / wave['start_price'] * 100
            else:  # down
                amplitude = (wave['start_price'] - wave['end_price']) / wave['start_price'] * 100
            
            # Calculate duration
            duration_days = (wave['end_date'] - wave['start_date']).days
            
            wave_stats.append({
                'wave_type': wave['wave_type'],
                'start_date': wave['start_date'].strftime('%Y-%m-%d'),
                'start_price': wave['start_price'],
                'end_date': wave['end_date'].strftime('%Y-%m-%d'),
                'end_price': wave['end_price'],
                'amplitude': amplitude,
                'duration_days': duration_days,
                'drawdown': amplitude if wave['wave_type'] == 'down' else 0  # For down waves, amplitude is drawdown
            })
        
        return wave_stats
    
    def _get_current_wave_info(self, data: List[Dict[str, Any]], waves: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Get information about the current incomplete wave."""
        if not waves:
            return None
        
        current_wave = waves[-1]  # Last wave is the current (potentially incomplete) one
        if current_wave['wave_type'] == 'initial':
            # Still forming the first wave
            return None
        
        current_price = data[-1]['close']
        start_price = current_wave['start_price']
        end_price = current_wave['end_price']
        start_date = current_wave['start_date']
        end_date = current_wave['end_date']
        
        if current_wave['wave_type'] == 'up':
            # In an up wave
            if end_price != start_price:  # Avoid division by zero
                progress = (current_price - start_price) / (end_price - start_price) * 100
            else:
                progress = 0
            current_wave_info = {
                'status': '上升波段中',
                'wave_type': 'up',
                'progress': progress,
                'current_price': current_price,
                'start_price': start_price,
                'start_date': start_date,
                'end_price': end_price,
                'end_date': end_date,
                'remaining_amplitude': end_price - current_price
            }
        else:
            # In a down wave
            if start_price != end_price:  # Avoid division by zero
                progress = (start_price - current_price) / (start_price - end_price) * 100
            else:
                progress = 0
            current_wave_info = {
                'status': '下降波段中',
                'wave_type': 'down',
                'progress': progress,
                'current_price': current_price,
                'start_price': start_price,
                'start_date': start_date,
                'end_price': end_price,
                'end_date': end_date,
                'drawdown_from_start': current_price - start_price
            }
        
        return current_wave_info
    
    def _calculate_current_drawdown(self, data: List[Dict[str, Any]]) -> float:
        """Calculate current price drawdown from recent high."""
        if len(data) < 2:
            return 0
        
        current_price = data[-1]['close']
        # Find the highest high from the beginning up to current date
        recent_highs = [p['high'] for p in data]
        if recent_highs:
            last_high = max(recent_highs)
            if last_high != 0:
                current_drawdown = (last_high - current_price) / last_high * 100
            else:
                current_drawdown = 0
        else:
            current_drawdown = 0
        
        return current_drawdown