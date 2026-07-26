#!/usr/bin/env python3
"""DramaLex · diagnose.py — 学前诊断（Pre-learning Diagnostic）

目的：让用户在开始学一集之前，先明确自己的英文水平档位（CEFR A1–C2）。
档位只校准「任务难度」，不筛词（诚实档位原则），但它是整条学习闭环的起点。

两种用法：
  1) 凭考试分数直接定位（最常见）：
       python diagnose.py --ielts 6.5
       python diagnose.py --toefl 90
       python diagnose.py --cet "CET-6"
       python diagnose.py --by-cefr B1
     也可组合：--ielts 5.5 --toefl 80（多条证据取最保守档位）。
  2) 自适应自测小测（无分数时）：
       python diagnose.py --quiz            # 交互问答
       python diagnose.py --quiz --answers 1,1,2,1,2,1,2,1,1,2,2,1   # 非交互（便于 agent/CI 测试）

输出 diagnose.json（被 run_episode.py prepare --diagnose 读取，自动设 --cefr）。

纯标准库。
"""
import argparse, json, os, sys, datetime

# 反向映射来自 exam_map
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import exam_map as exm

LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

# 自适应自测题库：每级 2 题，难度递进。option 首项为正确答案（answer 存索引，0-based）。
QUIZ = [
    # A1
    {"level": "A1", "q": "He ___ a teacher.", "options": ["is", "am", "are"], "answer": 0},
    {"level": "A1", "q": "I ___ coffee every morning.", "options": ["drink", "drinks", "drinking"], "answer": 0},
    # A2
    {"level": "A2", "q": "She has lived here ___ 2019.", "options": ["since", "for", "from"], "answer": 0},
    {"level": "A2", "q": "If it ___, we will stay home.", "options": ["rains", "rained", "will rain"], "answer": 0},
    # B1
    {"level": "B1", "q": "I'm used to ___ early.", "options": ["getting up", "get up", "got up"], "answer": 0},
    {"level": "B1", "q": "The report ___ by Friday.", "options": ["must be finished", "must finish", "must finished"], "answer": 0},
    # B2
    {"level": "B2", "q": "Not only ___ late, but he also forgot the file.", "options": ["was he", "he was", "were he"], "answer": 0},
    {"level": "B2", "q": "___ hard she tries, she can't please everyone.", "options": ["However", "No matter", "Whatever"], "answer": 0},
    # C1
    {"level": "C1", "q": "The proposal was met with ___ enthusiasm.", "options": ["a muted", "a muting", "muted"], "answer": 0},
    {"level": "C1", "q": "Had I known, I ___ differently.", "options": ["would have acted", "would act", "will act"], "answer": 0},
    # C2
    {"level": "C2", "q": "His argument, ___ persuasive on the surface, collapsed under scrutiny.", "options": ["albeit", "though being", "as if"], "answer": 0},
    {"level": "C2", "q": "The two theories are not so much complementary ___ mutually exclusive.", "options": ["as", "than", "but"], "answer": 0},
]


def run_quiz(answers=None):
    """返回 (cefr, detail)。detail 含每级正确数，便于解释。"""
    results = []  # (level, correct_bool)
    for i, item in enumerate(QUIZ):
        opts = item['options']
        if answers is not None and i < len(answers):
            chosen = answers[i]
        else:
            # 交互
            print(f"\n[{item['level']}] {item['q']}")
            for j, o in enumerate(opts):
                print(f"  {j+1}. {o}")
            while True:
                try:
                    v = input("  你的选择 (1-{}): ".format(len(opts))).strip()
                    chosen = int(v) - 1
                    if 0 <= chosen < len(opts):
                        break
                except ValueError:
                    pass
                print("  请输入数字。")
        correct = (chosen == item['answer'])
        results.append((item['level'], correct))

    # 逐级判定：某级「通过」= 该级 2 题至少对 1 题；
    # 推荐档位 = 连续通过的最高一级（A1 起，最低为 A1）。
    by_level = {}
    for lvl, ok in results:
        by_level.setdefault(lvl, []).append(ok)
    recommended = 'A1'
    for lvl in LEVEL_ORDER:
        graded = by_level.get(lvl, [])
        passed = sum(1 for x in graded if x) >= 1  # 至少对 1/2
        if passed:
            recommended = lvl
        else:
            break  # 一旦某级不通过，停止向上推（保守）
    # 分数统计
    total = sum(1 for _, ok in results if ok)
    detail = {
        "total": len(results),
        "correct": total,
        "by_level": {lvl: {"correct": sum(1 for x in v if x), "of": len(v)} for lvl, v in by_level.items()},
    }
    return recommended, detail


def build_output(cefr, source, evidence, quiz_detail=None):
    return {
        "cefr": cefr,
        "exam_label": exm.exam_label(cefr),
        "exam_tag": exm.exam_tag(cefr),
        "source": source,            # 'exam' | 'cefr' | 'quiz'
        "evidence": evidence,        # 例如 ["雅思6.5"] 或 ["quiz: 9/12"]
        "quiz_detail": quiz_detail,
        "note": ("档位仅校准任务难度，不自动筛词；低档位材料会用「挑战★」标注高阶词，"
                 "产出任务里会跳过它们。建议同时看字幕、循序渐进。"),
        "generated_at": datetime.datetime.now().isoformat(timespec='seconds'),
    }


def main():
    ap = argparse.ArgumentParser(description="DramaLex 学前诊断（CEFR A1–C2）")
    ap.add_argument('--ielts', default=None, help='雅思总分，如 6.5')
    ap.add_argument('--toefl', default=None, help='托福 iBT 总分，如 90')
    ap.add_argument('--cet', default=None, help='四六级/专四专八文字，如 "CET-6" / "专八"')
    ap.add_argument('--by-cefr', default=None, dest='by_cefr', help='直接指定档位 A1–C2')
    ap.add_argument('--quiz', action='store_true', help='跑自适应自测小测')
    ap.add_argument('--answers', default=None, help='非交互自测：逗号分隔的选项序号（1-based），如 1,1,2,1')
    ap.add_argument('--output', default='diagnose.json', help='输出文件路径')
    args = ap.parse_args()

    out = None
    if args.by_cefr:
        c = args.by_cefr.upper()
        if c not in LEVEL_ORDER:
            print(f"无效档位 {c}，应为 {LEVEL_ORDER}", file=sys.stderr); return 2
        out = build_output(c, 'cefr', [f"手动选档 {c}"])
    elif args.ielts or args.toefl or args.cet:
        cefr, used = exm.diagnose_from_exam(ielts=args.ielts, toefl=args.toefl, cet=args.cet)
        if not cefr:
            print("无法从给定分数定位档位（分数无法解析）。", file=sys.stderr); return 2
        ev = []
        if args.ielts: ev.append(f"雅思{args.ielts}")
        if args.toefl: ev.append(f"托福{args.toefl}")
        if args.cet: ev.append(f"{args.cet}")
        out = build_output(cefr, 'exam', ev)
    elif args.quiz:
        ans = None
        if args.answers:
            try:
                ans = [int(x) - 1 for x in args.answers.split(',') if x.strip() != '']
            except ValueError:
                print("answers 需为逗号分隔数字。", file=sys.stderr); return 2
        cefr, detail = run_quiz(ans)
        out = build_output(cefr, 'quiz', [f"自测 {detail['correct']}/{detail['total']}"], quiz_detail=detail)
    else:
        print("请指定一种诊断方式：--ielts / --toefl / --cet / --by-cefr / --quiz", file=sys.stderr)
        return 2

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"✅ 学前诊断结果：CEFR = {out['cefr']}（约 {out['exam_label']}）")
    print(f"   来源：{out['source']} · 证据：{', '.join(out['evidence'])}")
    print(f"   已写入 {args.output}")
    if out.get('quiz_detail'):
        d = out['quiz_detail']
        print(f"   自测正确率：{d['correct']}/{d['total']} · 分级："
              + " · ".join(f"{k} {v['correct']}/{v['of']}" for k, v in d['by_level'].items()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
