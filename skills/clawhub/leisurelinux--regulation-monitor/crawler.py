#!/usr/bin/env python3
"""
regulation-monitor / 监管动态追踪爬虫 v2.0

抓取中国金融监管机构最新动态：
  NFRA  — 国家金融监督管理总局（API + cloudscraper）
  CSRC  — 中国证券监督管理委员会（静态 HTML）
  PBOC  — 中国人民银行（静态 HTML）
  SAFE  — 国家外汇管理局（静态 HTML）
  MIIT  — 工业和信息化部（CMS API JSON）
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta

# ── 依赖检查 ──────────────────────────────────────────────
try:
    import cloudscraper
    _HAS_CS = True
except ImportError:
    _HAS_CS = False

try:
    import requests
except ImportError:
    print("❌ pip install requests beautifulsoup4 lxml cloudscraper", file=sys.stderr)
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ pip install beautifulsoup4 lxml", file=sys.stderr)
    sys.exit(1)

# ── 导航过滤 ──────────────────────────────────────────────
NAV = [
    '首页', '网站地图', 'RSS', 'English', '无障碍', '手机',
    '更新日志', '常见问题', '术语表', '广西', '海南', '重庆',
    '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海',
    '宁夏', '新疆', '深圳', '大连', '宁波', '厦门', '青岛',
    '上海专员办', '深圳专员办',
    '上海证券', '深圳证券', '北京证券', '上海期货', '郑州商品',
    '大连商品', '中国金融期货', '广州期货',
    '登记结算', '投资者保护', '市场监控', '中证数据', '全国中小',
    '证券业协会', '期货业协会', '上市公司协会', '投资基金业协会',
    '信息技术', '中小投资者', '商品指数', '金融研究院', '资本市场学院',
    '资本市场学会',
]


def is_nav(t):
    t = t.strip()
    if len(t) <= 4:
        return True
    for k in NAV:
        if k in t:
            return True
    return False


# ══════════════════════════════════════════════════════════
#  RegulationCrawler
# ══════════════════════════════════════════════════════════

class RegulationCrawler:

    def __init__(self, proxy=None, delay=1.5):
        self.delay = delay
        self.proxy = proxy
        self._http()

    def _http(self):
        """初始化 HTTP 客户端"""
        if _HAS_CS:
            self.cs = cloudscraper.create_scraper()
            self.cs.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            })
            if self.proxy:
                self.cs.proxies = {'http': self.proxy, 'https': self.proxy}

        self.s = requests.Session()
        self.s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        if self.proxy:
            self.s.proxies = {'http': self.proxy, 'https': self.proxy}

    # ──────────────── NFRA ────────────────

    def _nfra(self, days):
        if not _HAS_CS:
            return []
        cutoff = datetime.now() - timedelta(days=days)
        items = []
        for iid in [(925, '通知公告'), (923, '公示公告')]:
            s = cloudscraper.create_scraper()
            s.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            })
            if self.proxy:
                s.proxies = {'http': self.proxy, 'https': self.proxy}
            try:
                s.get('https://www.nfra.gov.cn/', timeout=30)
            except Exception:
                pass
            time.sleep(2)
            hdrs = {
                'Referer': 'https://www.nfra.gov.cn/cn/view/pages/ItemList.html',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
            }
            page = 1
            while page <= 3:
                try:
                    r = s.get(
                        'https://www.nfra.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild',
                        params={'itemId': iid[0], 'pageSize': 50, 'pageIndex': page},
                        headers=hdrs, timeout=30,
                    )
                except Exception as e:
                    print(f'  ⚠️ NFRA 请求异常: {e}', file=sys.stderr)
                    break
                if r.status_code != 200:
                    print(f'  ⚠️ NFRA {r.status_code}，重试…', file=sys.stderr)
                    time.sleep(5)
                    try:
                        s.get('https://www.nfra.gov.cn/', timeout=30)
                        time.sleep(2)
                        r = s.get(
                            'https://www.nfra.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild',
                            params={'itemId': iid[0], 'pageSize': 50, 'pageIndex': page},
                            headers=hdrs, timeout=30,
                        )
                    except Exception:
                        pass
                    if r.status_code != 200:
                        print(f'  ⚠️ NFRA 重试失败，跳过 {iid[1]}', file=sys.stderr)
                        break
                data = r.json()
                rows = (data.get('data') or {}).get('rows') or []
                total = (data.get('data') or {}).get('total') or 0
                if not rows:
                    break
                more = True
                for row in rows:
                    title = (row.get('docTitle') or '').strip()
                    if not title:
                        continue
                    dt = (row.get('publishDate') or '').strip()[:10]
                    did = row.get('docId')
                    url = f'https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId={did}&itemId={iid[0]}'
                    d = self._pdate(dt)
                    if d and d < cutoff:
                        more = False
                        break
                    items.append(dict(title=title, url=url, date=dt,
                                      regulator='nfra', regulator_name='国家金融监督管理总局'))
                if not more:
                    break
                if page * 50 >= total:
                    break
                page += 1
                time.sleep(self.delay + 1)
        return items

    # ──────────────── CSRC ────────────────

    def _csrc(self, days):
        return self._html([
            'http://www.csrc.gov.cn/csrc/c100028/common_list.shtml',
            'http://www.csrc.gov.cn/csrc/c100028/common_list2.shtml',
        ], 'csrc', '中国证券监督管理委员会', 'http://www.csrc.gov.cn', days)

    # ──────────────── PBOC ────────────────

    def _pboc(self, days):
        return self._html([
            'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html',
        ], 'pboc', '中国人民银行', 'http://www.pbc.gov.cn', days)

    # ──────────────── SAFE 外管局 ──────────

    def _safe(self, days):
        """外管局 — 静态 HTML 列表页"""
        urls = [
            ('https://www.safe.gov.cn/safe/tbts/index.html', '公告信息'),
            ('https://www.safe.gov.cn/safe/zcfg/index.html', '政策法规'),
            ('https://www.safe.gov.cn/safe/whxw/index.html', '外汇新闻'),
        ]
        cutoff = datetime.now() - timedelta(days=days)
        items = []
        for url, label in urls:
            print(f'  请求: {url}', file=sys.stderr)
            html = self._get(url)
            if not html:
                continue
            soup = BeautifulSoup(html, 'lxml')
            n = 0
            for li in soup.find_all('li'):
                a = li.find('a')
                if not a or not a.get('href'):
                    continue
                title = (a.get('title') or a.get_text(strip=True) or '').strip()
                href = a['href']
                if not title or is_nav(title):
                    continue
                date = ''
                dm = re.search(r'(\d{4}[-/]\d{1,2}[-/]\d{1,2})', li.get_text())
                if dm:
                    date = dm.group(1)
                if not date:
                    continue
                url_full = self._abs(href, 'https://www.safe.gov.cn')
                d = self._pdate(date)
                if d and d < cutoff:
                    continue
                items.append(dict(title=title, url=url_full, date=date,
                                  regulator='safe', regulator_name='国家外汇管理局'))
                n += 1
            print(f'  +{n} 条（{label}）', file=sys.stderr)
            time.sleep(self.delay)
        return items

    # ──────────────── MIIT 工信部 ──────────

    def _miit(self, days):
        """工信部 — CMS API JSON"""
        base = 'https://www.miit.gov.cn/api-gateway/jpaas-publish-server/front/page/build/unit'
        # webId 和 tplSetId 全站统一
        web_id = '8d828e408d90447786ddbe128d495e9e'
        tpl_set = '209741b2109044b5b7695700b2bec37e'
        columns = [
            ('42cd38164cb6441a84bdfa441909e15e', '最新政策'),
            ('3e3ad1a3bec74939890a0d3e54815141', '通知公告'),
        ]
        cutoff = datetime.now() - timedelta(days=days)
        items = []
        for page_id, label in columns:
            print(f'  请求 MIIT API: {label}', file=sys.stderr)
            try:
                r = self.s.get(base, params={
                    'parseType': 'buildstatic',
                    'webId': web_id,
                    'tplSetId': tpl_set,
                    'pageType': 'column',
                    'tagId': '右侧内容',
                    'editType': 'null',
                    'pageId': page_id,
                }, headers={
                    'Referer': 'https://www.miit.gov.cn/',
                    'Accept': 'application/json',
                }, timeout=15)
            except Exception as e:
                print(f'  ⚠️ MIIT API 异常: {e}', file=sys.stderr)
                continue
            if r.status_code != 200:
                print(f'  ⚠️ MIIT API {r.status_code}', file=sys.stderr)
                continue
            try:
                data = r.json()
            except Exception:
                print(f'  ⚠️ MIIT JSON 解析失败', file=sys.stderr)
                continue
            html = (data.get('data') or {}).get('html', '')
            if not html:
                continue
            soup = BeautifulSoup(html, 'lxml')
            n = 0
            for li in soup.find_all('li'):
                a = li.find('a')
                if not a or not a.get('href'):
                    continue
                title = (a.get('title') or a.get_text(strip=True) or '').strip()
                href = a['href']
                if not title or is_nav(title):
                    continue
                span = li.find('span')
                date = span.get_text(strip=True) if span else ''
                if not date:
                    continue
                url_full = self._abs(href, 'https://www.miit.gov.cn')
                d = self._pdate(date)
                if d and d < cutoff:
                    continue
                items.append(dict(title=title, url=url_full, date=date,
                                  regulator='miit', regulator_name='工业和信息化部'))
                n += 1
            print(f'  +{n} 条（{label}）', file=sys.stderr)
            time.sleep(self.delay)
        return items

    # ──────────────── 通用 HTML ────────────

    def _html(self, urls, code, name, base, days):
        cutoff = datetime.now() - timedelta(days=days)
        items = []
        for url in urls:
            print(f'  请求: {url}', file=sys.stderr)
            html = self._get(url)
            if not html:
                continue
            soup = BeautifulSoup(html, 'lxml')
            n = 0
            for tag in soup.find_all(['li', 'tr']):
                a = tag.find('a')
                if not a or not a.get('href'):
                    continue
                title = (a.get('title') or a.get_text(strip=True) or '').strip()
                href = a['href']
                if not title or is_nav(title):
                    continue
                date = ''
                dm = re.search(r'(\d{4}[-/]\d{1,2}[-/]\d{1,2})', tag.get_text())
                if dm:
                    date = dm.group(1)
                if not date:
                    continue
                url_full = self._abs(href, base)
                d = self._pdate(date)
                if d and d < cutoff:
                    continue
                items.append(dict(title=title, url=url_full, date=date,
                                  regulator=code, regulator_name=name))
                n += 1
            print(f'  +{n} 条', file=sys.stderr)
            time.sleep(self.delay)
        return items

    def _get(self, url, enc='utf-8'):
        try:
            r = self.s.get(url, timeout=30)
            r.encoding = r.apparent_encoding or enc
            return r.text
        except Exception as e:
            print(f'  ⚠️ {e}', file=sys.stderr)
            return None

    @staticmethod
    def _abs(href, base):
        if href.startswith('http://') or href.startswith('https://'):
            return href
        if href.startswith('//'):
            return 'http:' + href
        if href.startswith('/'):
            return base.rstrip('/') + '/' + href.lstrip('/')
        return base.rstrip('/') + '/' + href

    @staticmethod
    def _pdate(s):
        s = s.strip().replace('年', '-').replace('月', '-').replace('日', '')
        for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d', '%Y%m%d']:
            try:
                return datetime.strptime(s, fmt)
            except ValueError:
                continue
        m = re.search(r'(\d{4})\D?(\d{1,2})\D?(\d{1,2})', s)
        if m:
            try:
                return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            except ValueError:
                pass
        return None

    # ── 主入口 ────────────────────────────────────────────

    def crawl(self, regulator='all', days=7, summary=False):
        all_items = []

        regs = {
            'nfra': ('国家金融监督管理总局', self._nfra),
            'csrc': ('中国证券监督管理委员会', self._csrc),
            'pboc': ('中国人民银行', self._pboc),
            'safe': ('国家外汇管理局', self._safe),
            'miit': ('工业和信息化部', self._miit),
        }

        if regulator == 'all':
            keys = list(regs.keys())
        else:
            keys = [regulator]

        for k in keys:
            if k not in regs:
                print(f'  ⚠️ 未知机构: {k}', file=sys.stderr)
                continue
            name, fn = regs[k]
            print(f'🔍 正在抓取 {name}…', file=sys.stderr)
            items = fn(days)
            print(f'  ✅ {name}: {len(items)} 条', file=sys.stderr)
            all_items.extend(items)

        # 去重+排序
        seen, uniq = set(), []
        for it in all_items:
            if it['url'] not in seen:
                seen.add(it['url'])
                uniq.append(it)
        uniq.sort(key=lambda x: self._pdate(x['date']) or datetime.min, reverse=True)

        if summary and uniq:
            print('\n📝 抓取摘要…', file=sys.stderr)
            for i, it in enumerate(uniq):
                print(f'  [{i+1}/{len(uniq)}] {it["title"][:40]}', file=sys.stderr)
                it['summary'] = self._sum(it['url'])
                time.sleep(1)
        return uniq

    def _sum(self, url, n=200):
        try:
            r = self.s.get(url, timeout=15)
            r.encoding = r.apparent_encoding or 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')
            for t in soup(['script', 'style', 'nav', 'footer', 'header']):
                t.decompose()
            for sel in ['.article-content', '.content', '.main-text', '#content',
                        '.detail-content', '.news-content', 'article', 'body']:
                b = soup.select_one(sel)
                if b:
                    t = re.sub(r'\s+', ' ', b.get_text(strip=True))
                    if len(t) > 50:
                        return t[:n] + ('…' if len(t) > n else '')
            return ''
        except Exception:
            return ''


# ══════════════════════════════════════════════════════════
#  输出
# ══════════════════════════════════════════════════════════

def fmt(items, json_flag=False):
    if json_flag:
        return json.dumps(items, ensure_ascii=False, indent=2)
    if not items:
        return '## 监管动态\n\n📭 未找到。'
    g = {}
    for it in items:
        g.setdefault(it.get('regulator_name', '未知'), []).append(it)
    lines = ['# 📊 金融监管动态追踪\n']
    lines.append(f'> {datetime.now().strftime("%Y-%m-%d %H:%M")} | {len(items)} 条\n')
    for name, its in g.items():
        lines.append(f'## 🏛️ {name}（{len(its)}）\n')
        for it in its:
            s = it.get('summary', '')
            lines.append(f'### [📌 {it["title"]}]({it["url"]})\n')
            lines.append(f'- **机构：** {name}')
            lines.append(f'- **日期：** {it.get("date", "?")}')
            if s:
                lines.append(f'- **摘要：** {s}')
            lines.append('\n---\n')
    lines.append('## 📈 趋势\n')
    lines.append(f'> {len(items)} 条动态，{len(g)} 个机构。\n')
    return '\n'.join(lines)


# ══════════════════════════════════════════════════════════
#  CLI
# ══════════════════════════════════════════════════════════

def main():
    p = argparse.ArgumentParser(description='regulation-monitor v2.0')
    p.add_argument('-r', '--regulator', default='all',
                   choices=['all', 'nfra', 'csrc', 'pboc', 'safe', 'miit'])
    p.add_argument('-d', '--days', type=int, default=7, help='回溯天数')
    p.add_argument('-s', '--summary', action='store_true', help='抓取摘要')
    p.add_argument('-j', '--json', action='store_true', help='JSON 输出')
    p.add_argument('-p', '--proxy', help='代理地址')
    a = p.parse_args()

    c = RegulationCrawler(proxy=a.proxy)
    try:
        items = c.crawl(a.regulator, a.days, a.summary)
        print(fmt(items, a.json))
    except KeyboardInterrupt:
        print('\n⚠️ 中断', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
