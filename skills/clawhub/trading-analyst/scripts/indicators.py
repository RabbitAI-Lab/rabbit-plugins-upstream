#!/usr/bin/env python3
"""Lightweight indicator math (no external deps). All from a list of closes."""
import math

def ema(vals, period):
    if len(vals) < period: return None
    k = 2/(period+1)
    e = sum(vals[:period])/period
    for v in vals[period:]:
        e = v*k + e*(1-k)
    return round(e, 2)

def sma(vals, period):
    if len(vals) < period: return None
    return round(sum(vals[-period:])/period, 2)

def rsi(vals, period=14):
    if len(vals) < period+1: return None
    gains, losses = [], []
    for i in range(1, len(vals)):
        d = vals[i]-vals[i-1]
        gains.append(max(d,0)); losses.append(max(-d,0))
    ag = sum(gains[-period:])/period
    al = sum(losses[-period:])/period
    if al == 0: return 100.0
    rs = ag/al
    return round(100 - 100/(1+rs), 2)

def atr(highs, lows, closes, period=14):
    if len(closes) < period+1: return None
    trs = []
    for i in range(1, len(closes)):
        tr = max(highs[i]-lows[i], abs(highs[i]-closes[i-1]), abs(lows[i]-closes[i-1]))
        trs.append(tr)
    return round(sum(trs[-period:])/period, 2)

def macd(vals, fast=12, slow=26, sig=9):
    n = len(vals)
    if n < slow+1: return None, None, None
    kf, ks, kg = 2/(fast+1), 2/(slow+1), 2/(sig+1)
    # full EMA arrays of length n, seeded with SMA of first 'period'
    def ema_full(period):
        e = sum(vals[:period])/period
        arr = [e]*period
        for i in range(period, n):
            e = vals[i]*k + e*(1-k) if period == fast else vals[i]*k + e*(1-k)
        return arr
    # build properly
    ef = [0.0]*n; es = [0.0]*n
    ef[fast-1] = sum(vals[:fast])/fast; es[slow-1] = sum(vals[:slow])/slow
    for i in range(fast, n):
        ef[i] = vals[i]*kf + ef[i-1]*(1-kf)
    for i in range(slow, n):
        es[i] = vals[i]*ks + es[i-1]*(1-ks)
    macd_line = [ef[i]-es[i] for i in range(slow, n)]
    if len(macd_line) < sig: return None, None, None
    sig_line = [0.0]*len(macd_line)
    sig_line[sig-1] = sum(macd_line[:sig])/sig
    for i in range(sig, len(macd_line)):
        sig_line[i] = macd_line[i]*kg + sig_line[i-1]*(1-kg)
    last_macd = macd_line[-1]; last_sig = sig_line[-1]
    hist = round(last_macd - last_sig, 2)
    return round(last_macd, 2), round(last_sig, 2), hist

def stochastic(highs, lows, closes, k_period=14, d_period=3):
    if len(closes) < k_period: return None, None
    hh = max(highs[-k_period:]); ll = min(lows[-k_period:])
    if hh == ll: return 50.0, 50.0
    last = closes[-1]
    k = (last - ll)/(hh - ll)*100
    # %D = SMA3 of %K
    ks = []
    for i in range(d_period):
        idx = -(i+1)
        hhi = max(highs[idx-k_period:idx] or highs[-k_period:])
        lli = min(lows[idx-k_period:idx] or lows[-k_period:])
        if hhi == lli: ks.append(50.0)
        else: ks.append((closes[idx]-lli)/(hhi-lli)*100)
    d = sum(ks)/len(ks)
    return round(k, 2), round(d, 2)

def adx(highs, lows, closes, period=14):
    """Simplified ADX from candle data (true-range based + DI)."""
    if len(closes) < period*2: return None
    plus_dm, minus_dm, trs = [], [], []
    for i in range(1, len(closes)):
        up = highs[i]-highs[i-1]
        dn = lows[i-1]-lows[i]
        plus_dm.append(max(up,0) if up>dn else 0)
        minus_dm.append(max(dn,0) if dn>up else 0)
        tr = max(highs[i]-lows[i], abs(highs[i]-closes[i-1]), abs(lows[i]-closes[i-1]))
        trs.append(tr)
    atr_ = sum(trs[-period:])/period
    if atr_ == 0: return None
    pd = sum(plus_dm[-period:])/period/atr_
    md = sum(minus_dm[-period:])/period/atr_
    dx = abs(pd-md)/(pd+md)*100 if (pd+md)>0 else 0
    # smoothed ADX (single window ok for our purpose)
    return round(dx, 1)

def fib(levels, hi, lo):
    diff = hi - lo
    return {str(l): round(hi - diff*l, 2) for l in levels}

def pivot(highs, lows, closes):
    if len(closes) < 2: return None
    h, l, c = highs[-1], lows[-1], closes[-1]
    p = (h+l+c)/3
    r1 = 2*p - l; s1 = 2*p - h
    r2 = p + (h-l); s2 = p - (h-l)
    r3 = h + 2*(p-l); s3 = l - 2*(h-p)
    return {"P": round(p,2), "R1": round(r1,2), "R2": round(r2,2), "R3": round(r3,2),
            "S1": round(s1,2), "S2": round(s2,2), "S3": round(s3,2)}

def swings(highs, lows, n=20):
    """Return last n-candle swing high/low extremes."""
    if len(highs) < n: n = len(highs)
    return max(highs[-n:]), min(lows[-n:])
