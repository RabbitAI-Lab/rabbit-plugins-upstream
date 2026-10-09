# -*- coding: utf-8 -*-
"""
综合审稿（review_all）—— 一次跑完全部门禁，输出一份审核报告

串联维度：
    humanizer   去 AI 痕迹（humanizer_check.py，FAIL 项必须改写）
    scale       规模审查（字数达标）
    continuity  一致性审稿（专名异写／角色属性／时间线／标题与正文）
    rationality 合理化审查（重复段落／对话占比／视角／伏笔／大纲覆盖）
    punctuation 标点审查（引号错位／半角标点／繁体／英文残留／密度）

用法（在子项目根目录执行）：
    python "../GitHub Novel Serialization Skill/scripts/review_all.py"
    python "../GitHub Novel Serialization Skill/scripts/review_all.py" --chapters 031 034 036
    python "../GitHub Novel Serialization Skill/scripts/review_all.py" --draft notes-personal/第一卷正文草稿.md --batch "第9批"
    python "../GitHub Novel Serialization Skill/scripts/review_all.py" --out .workbuddy/reports/草稿审核报告_2026-09-27.md
    python "../GitHub Novel Serialization Skill/scripts/review_all.py" --skip humanizer,scale

判定：任一维度 FAIL → 综合 FAIL（不得进定稿）；有 WARN → REVISE（人工复核）；否则 PASS。
"""
import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _review_lib as L
import humanizer_check
import review_scale
import review_continuity
import review_rationality
import review_punctuation

DIMS = [('humanizer', '去 AI 痕迹'), ('scale', '规模审查'), ('continuity', '一致性审稿'),
        ('rationality', '合理化审查'), ('punctuation', '标点审查')]


def run_humanizer(root, cfg):
    """复用 humanizer_check.check_file：定稿逐章单检，草稿按整份折算（等价章数）"""
    items = L.collect_items(root, cfg.get('chapters', ()), cfg.get('draft', ''))
    issues = []

    def collect(path, where):
        for lv, label, cnt, samples in humanizer_check.check_file(path)['issues']:
            loc = '、'.join('L%d:%s' % (a, b) for a, b in samples[:2])
            issues.append(L.Issue(lv, 'AI痕迹·%s' % label, '%s 处 %s' % (cnt, loc), where))

    if cfg.get('draft', ''):
        p = cfg['draft']
        collect(p if os.path.isabs(p) else os.path.join(root, p), '整份草稿')
    else:
        for it in items:
            collect(it.path, it.name)
    return issues


def run_dim(name, root, cfg):
    if name == 'humanizer':
        return run_humanizer(root, cfg)
    mod = {'scale': review_scale, 'continuity': review_continuity,
           'rationality': review_rationality, 'punctuation': review_punctuation}[name]
    results, _ = mod.run(root, cfg)
    issues = []
    for r in results:
        for i in r.issues:
            issues.append(L.Issue(i.level, i.category, i.detail, i.where or r.name))
    return issues


def todo_list(results):
    lines = []
    for r in results:
        for i in sorted(r.issues, key=lambda x: L.LEVEL_ORDER.get(x.level, 0), reverse=True):
            lines.append('- [ ] [%s] %s：%s —— %s' % (i.level, i.where or r.name, i.category, i.detail))
    return '\n'.join(lines) or '无待办。'


def main():
    ap = L.add_common_args(argparse.ArgumentParser(description='综合审稿：一次跑完全部门禁'))
    ap.add_argument('--batch', default='', help='批次名（写入报告标题，如「第9批」）')
    ap.add_argument('--skip', default='', help='跳过的维度，逗号分隔，如 humanizer,scale')
    ap.add_argument('--target', type=int, default=4000, help='每章目标字数（默认 4000）')
    ap.add_argument('--max', type=int, default=0, help='每章字数上限（0 = 不限）')
    a = ap.parse_args()
    root = L.find_root(a.root)
    skip = {s.strip() for s in a.skip.split(',') if s.strip()}
    cfg = {'chapters': a.chapters, 'draft': a.draft, 'root': root,
           'target': a.target, 'max': a.max}

    results, scale_sum = [], ''
    for key, label in DIMS:
        if key in skip:
            continue
        issues = run_dim(key, root, cfg)
        results.append(L.make_result(label, '', issues))
        if key == 'scale':
            _, scale_sum = review_scale.run(root, cfg)

    title = '综合审稿报告' + ('（%s）' % a.batch if a.batch else '')
    intro = ['- 审查范围：%s' % (a.draft or 'chapters/ 定稿'),
             '- 参与维度：%s' % '、'.join(r.name for r in results),
             '- 门禁：任一 FAIL 不得同步定稿；WARN 需人工复核后方可送审']
    extra = []
    if scale_sum:
        extra.append(('规模概览', scale_sum))
    extra.append(('待办清单（按严重度排序）', todo_list(results)))
    md = L.render(title, results, intro=intro, extra_sections=extra, obj_label='审查维度')
    L.emit(md, a.out or None)
    v = L.verdict(results)
    print('\n>>> 综合判定：%s' % v)
    return 0 if v != 'FAIL' else 2


if __name__ == '__main__':
    sys.exit(main())
