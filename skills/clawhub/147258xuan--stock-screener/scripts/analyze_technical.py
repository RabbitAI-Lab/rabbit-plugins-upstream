#!/usr/bin/env python3
"""
技术面分析脚本：对给定股票列表计算均线/MACD/RSI/布林带/涨跌停状态
使用腾讯财经K线接口，输出JSON到stdout
"""
import requests
import json
import sys
import os

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://finance.sina.com.cn/'}

def fetch_kline(code, days=100):
    """Fetch daily K-line data from Sina API"""
    if code.startswith('sh') or code.startswith('sz'):
        sina_code = code
    else:
        sina_code = code
    
    url = f'https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={sina_code}&scale=240&ma=no&datalen={min(days, 120)}'
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            return None
        data = r.json()
        if not data or not isinstance(data, list):
            return None
        # Convert to list of dicts
        result = []
        for item in data:
            result.append({
                'date': item.get('day', ''),
                'open': float(item.get('open', 0)),
                'close': float(item.get('close', 0)),
                'high': float(item.get('high', 0)),
                'low': float(item.get('low', 0)),
                'volume': float(item.get('volume', 0)),
            })
        return result if result else None
    except Exception as e:
        return None

def calculate_ma(closes, window):
    if len(closes) < window:
        return None
    return sum(closes[-window:]) / window

def calculate_ema(values, span):
    if len(values) < span:
        return None
    ema = sum(values[:span]) / span
    multiplier = 2 / (span + 1)
    for v in values[span:]:
        ema = (v - ema) * multiplier + ema
    return ema

def calculate_macd(closes):
    if len(closes) < 26:
        return None
    ema12 = calculate_ema(closes, 12)
    ema26 = calculate_ema(closes, 26)
    if ema12 is None or ema26 is None:
        return None
    macd_line = ema12 - ema26
    # Signal line: EMA of MACD line (9 periods)
    # We need to compute MACD for all points to get the signal line
    macd_series = []
    for i in range(25, len(closes)):
        sub = closes[:i+1]
        e12 = calculate_ema(sub, 12)
        e26 = calculate_ema(sub, 26)
        if e12 is not None and e26 is not None:
            macd_series.append(e12 - e26)
    if len(macd_series) < 9:
        return None
    signal_line = calculate_ema(macd_series, 9)
    if signal_line is None:
        return None
    hist = (macd_line - signal_line) * 2
    # Previous values for cross detection
    prev_macd_series = macd_series[:-1]
    prev_signal = calculate_ema(prev_macd_series, 9) if len(prev_macd_series) >= 9 else None
    prev_hist = (macd_series[-1] - prev_signal) * 2 if prev_signal is not None else 0
    return {
        'macd': round(macd_line, 4),
        'signal': round(signal_line, 4),
        'hist': round(hist, 4),
        'prev_hist': round(prev_hist, 4),
    }

def calculate_rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [d if d > 0 else 0 for d in deltas[-period:]]
    losses = [-d if d < 0 else 0 for d in deltas[-period:]]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)

def calculate_bollinger(closes, window=20, num_std=2):
    if len(closes) < window:
        return None
    recent = closes[-window:]
    sma = sum(recent) / window
    variance = sum((x - sma) ** 2 for x in recent) / window
    std = variance ** 0.5
    return {
        'upper': round(sma + num_std * std, 2),
        'middle': round(sma, 2),
        'lower': round(sma - num_std * std, 2),
        'price': closes[-1],
    }

def check_limit_status(prev_close, current_price, is_st=False):
    if prev_close <= 0 or current_price <= 0:
        return 'normal', 0
    change_pct = (current_price - prev_close) / prev_close * 100
    limit_pct = 20.0 if is_st else 10.0
    if change_pct >= limit_pct - 0.5:
        return 'limit_up', change_pct
    elif change_pct <= -(limit_pct - 0.5):
        return 'limit_down', change_pct
    return 'normal', change_pct

def is_st_stock(name):
    return name and ('ST' in name or 'st' in name or '*ST' in name)

def analyze_stock(code, name):
    result = {
        'code': code,
        'name': name,
        'ma_bullish': False,
        'ma_bearish': False,
        'macd_golden': False,
        'macd_death': False,
        'rsi_overbought': False,
        'rsi_oversold': False,
        'boll_breakout': False,
        'boll_breakdown': False,
        'limit_up': False,
        'limit_down': False,
        'change_pct': 0,
        'rsi': 0,
        'macd': 0,
        'error': None,
    }

    klines = fetch_kline(code, days=100)
    if not klines or len(klines) < 30:
        result['error'] = 'insufficient data'
        return result

    closes = [k['close'] for k in klines]
    current_price = closes[-1]
    prev_close = closes[-2]

    # MA
    ma5 = calculate_ma(closes, 5)
    ma10 = calculate_ma(closes, 10)
    ma20 = calculate_ma(closes, 20)
    if ma5 and ma10 and ma20:
        result['ma_bullish'] = ma5 > ma10 > ma20
        result['ma_bearish'] = ma5 < ma10 < ma20

    # MACD
    macd_data = calculate_macd(closes)
    if macd_data:
        result['macd'] = macd_data['macd']
        result['macd_golden'] = macd_data['prev_hist'] < 0 and macd_data['hist'] > 0
        result['macd_death'] = macd_data['prev_hist'] > 0 and macd_data['hist'] < 0

    # RSI
    rsi_val = calculate_rsi(closes)
    if rsi_val is not None:
        result['rsi'] = rsi_val
        result['rsi_overbought'] = rsi_val > 70
        result['rsi_oversold'] = rsi_val < 30

    # Bollinger
    boll = calculate_bollinger(closes)
    if boll:
        result['boll_breakout'] = boll['price'] > boll['upper']
        result['boll_breakdown'] = boll['price'] < boll['lower']

    # Limit status
    limit_status, change_pct = check_limit_status(prev_close, current_price, is_st_stock(name))
    result['limit_up'] = (limit_status == 'limit_up')
    result['limit_down'] = (limit_status == 'limit_down')
    result['change_pct'] = round(change_pct, 2)

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_technical.py <codes_json_file> [output_json_file]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_path, 'r', encoding='utf-8') as f:
        stocks = json.load(f)

    print(f"Analyzing {len(stocks)} stocks...", file=sys.stderr)
    results = []
    for i, stock in enumerate(stocks):
        code = stock['code']
        name = stock['name']
        res = analyze_stock(code, name)
        results.append(res)
        if (i + 1) % 10 == 0:
            print(f"  Progress: {i+1}/{len(stocks)}", file=sys.stderr)

    output = json.dumps(results, ensure_ascii=False)
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Saved to {output_path}", file=sys.stderr)
    else:
        print(output)

if __name__ == '__main__':
    main()
