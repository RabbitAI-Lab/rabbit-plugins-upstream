#!/usr/bin/env python3
"""
原型完整性验证脚本
检查生成的原型文档是否满足完整性要求

用法：
    python validate_prototype.py <prototype_path> <prd_path> [api_doc_path]

输出：
    - 验证通过项（绿色）
    - 验证失败项（红色，附带原因）
    - 待确认清单（黄色）
    - 验证报告 Markdown 片段
"""

import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple


class PrototypeValidator:
    """原型文档验证器"""
    
    def __init__(self, prototype_path: str, prd_path: str, api_doc_path: str = None):
        self.prototype_path = Path(prototype_path)
        self.prd_path = Path(prd_path)
        self.api_doc_path = Path(api_doc_path) if api_doc_path else None
        
        self.prototype_content = ""
        self.prd_content = ""
        self.api_content = ""
        
        self.results: List[Dict] = []
    
    def load_files(self):
        """加载所有文件内容"""
        with open(self.prototype_path, 'r', encoding='utf-8') as f:
            self.prototype_content = f.read()
        
        with open(self.prd_path, 'r', encoding='utf-8') as f:
            self.prd_content = f.read()
        
        if self.api_doc_path and self.api_doc_path.exists():
            with open(self.api_doc_path, 'r', encoding='utf-8') as f:
                self.api_content = f.read()
    
    def check_structure(self) -> Dict:
        """检查文档结构完整性"""
        required_sections = [
            ("页面清单", r"##?\s*1\.?\s*页面清单"),
            ("全局规范", r"##?\s*2\.?\s*全局规范"),
            ("核心页面原型", r"##?\s*3\.?\s*核心页面"),
            ("业务流程", r"##?\s*4\.?\s*业务"),
            ("数据与接口对照", r"##?\s*5\.?\s*数据"),
        ]
        
        missing = []
        for name, pattern in required_sections:
            if not re.search(pattern, self.prototype_content, re.IGNORECASE):
                missing.append(name)
        
        return {
            "check": "文档结构",
            "status": "pass" if not missing else "fail",
            "detail": f"包含 {5 - len(missing)}/5 个必需章节" + 
                     (f"，缺失：{', '.join(missing)}" if missing else ""),
            "missing": missing
        }
    
    def check_page_completeness(self) -> Dict:
        """检查页面完整性（每个页面是否有布局、字段、交互）"""
        # 匹配 ### 3.x 页面名 格式
        page_sections = re.findall(
            r'###\s*\d+\.\d+\s*(.+?)\n(.*?)(?=###\s*\d+\.\d+|##\s*\d)',
            self.prototype_content,
            re.DOTALL
        )
        
        incomplete_pages = []
        for page_name, page_content in page_sections:
            checks = {
                "布局": bool(re.search(r'布局|结构|框架|┌|│|└', page_content)),
                "字段": bool(re.search(r'字段|列|属性|表单|输入', page_content)),
                "交互": bool(re.search(r'交互|点击|操作|筛选|排序|分页', page_content)),
            }
            
            missing = [k for k, v in checks.items() if not v]
            if missing:
                incomplete_pages.append(f"{page_name.strip()}（缺：{', '.join(missing)}）")
        
        return {
            "check": "页面完整性",
            "status": "pass" if not incomplete_pages else "warn",
            "detail": f"检查 {len(page_sections)} 个页面，" +
                     (f"{len(incomplete_pages)} 个不完整" if incomplete_pages else "全部完整"),
            "incomplete": incomplete_pages
        }
    
    def check_prd_coverage(self) -> Dict:
        """检查 PRD 需求覆盖率"""
        # 从 PRD 中提取关键功能点（简化版：提取加粗/列表项）
        prd_features = set()
        
        # 提取 "###" 或 "##" 标题作为功能点
        prd_sections = re.findall(r'##+\s*(.+)', self.prd_content)
        for section in prd_sections:
            # 清理并取关键词
            keywords = re.findall(r'[\u4e00-\u9fa5]{2,}', section)
            prd_features.update(keywords)
        
        # 检查原型中是否提及这些功能
        uncovered = []
        for feature in prd_features:
            # 取前4个字作为匹配关键词
            keyword = feature[:4]
            if len(keyword) >= 2 and keyword not in self.prototype_content:
                uncovered.append(feature)
        
        # 限制报告数量，避免过多
        uncovered_sample = uncovered[:10]
        
        return {
            "check": "PRD需求覆盖",
            "status": "pass" if len(uncovered) < 5 else "warn",
            "detail": f"PRD提取 {len(prd_features)} 个功能关键词，" +
                     f"疑似未覆盖 {len(uncovered)} 个" +
                     (f"（示例：{', '.join(uncovered_sample)}）" if uncovered_sample else ""),
            "uncovered_count": len(uncovered)
        }
    
    def check_exception_states(self) -> Dict:
        """检查异常状态覆盖"""
        exception_keywords = {
            "空状态": r"空状态|暂无数据|empty",
            "加载状态": r"加载|Loading|Skeleton| Spin ",
            "错误状态": r"错误|失败|Error|异常",
            "无权限": r"无权限|未授权| forbidden ",
        }
        
        found = []
        missing = []
        for name, pattern in exception_keywords.items():
            if re.search(pattern, self.prototype_content, re.IGNORECASE):
                found.append(name)
            else:
                missing.append(name)
        
        return {
            "check": "异常状态覆盖",
            "status": "pass" if len(missing) <= 1 else "warn",
            "detail": f"覆盖 {len(found)}/4 种异常状态" +
                     (f"，缺失：{', '.join(missing)}" if missing else ""),
            "missing": missing
        }
    
    def check_api_alignment(self) -> Dict:
        """检查接口对齐（如有接口文档）"""
        if not self.api_content:
            return {
                "check": "接口对齐",
                "status": "skip",
                "detail": "未提供接口文档，跳过此项检查",
            }
        
        # 简单检查：原型中是否有接口映射章节
        has_mapping = bool(re.search(r'接口映射|接口对照|API对照', self.prototype_content))
        
        return {
            "check": "接口对齐",
            "status": "pass" if has_mapping else "warn",
            "detail": "已包含接口映射章节" if has_mapping else "未找到接口映射章节",
        }
    
    def check_workflow_closure(self) -> Dict:
        """检查业务流程闭环"""
        # 查找流程章节
        workflow_sections = re.findall(
            r'###\s*\d+\.\d+\s*(.+?流程.+?)\n(.*?)(?=###\s*\d+\.\d+|##\s*\d)',
            self.prototype_content,
            re.DOTALL | re.IGNORECASE
        )
        
        issues = []
        for flow_name, flow_content in workflow_sections:
            # 检查是否有异常分支
            if not re.search(r'异常|错误|失败|取消|驳回', flow_content, re.IGNORECASE):
                issues.append(f"{flow_name.strip()}（缺异常分支）")
            
            # 检查是否有边界情况
            if not re.search(r'边界|极端|空值|最大|最小|限制', flow_content, re.IGNORECASE):
                issues.append(f"{flow_name.strip()}（缺边界情况）")
        
        return {
            "check": "流程闭环",
            "status": "pass" if len(issues) < 2 else "warn",
            "detail": f"检查 {len(workflow_sections)} 个流程，" +
                     (f"{len(issues)} 处待完善" if issues else "全部完整"),
            "issues": issues
        }
    
    def run_all_checks(self) -> List[Dict]:
        """运行所有检查"""
        self.load_files()
        
        checks = [
            self.check_structure(),
            self.check_page_completeness(),
            self.check_prd_coverage(),
            self.check_exception_states(),
            self.check_api_alignment(),
            self.check_workflow_closure(),
        ]
        
        self.results = checks
        return checks
    
    def generate_report(self) -> str:
        """生成 Markdown 格式的验证报告"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "pass")
        warnings = sum(1 for r in self.results if r["status"] == "warn")
        failed = sum(1 for r in self.results if r["status"] == "fail")
        skipped = sum(1 for r in self.results if r["status"] == "skip")
        
        report = f"""## 原型验证报告

| 检查项 | 状态 | 说明 |
|--------|------|------|
"""
        
        status_icon = {
            "pass": "✅",
            "warn": "⚠️",
            "fail": "❌",
            "skip": "⏭️"
        }
        
        for result in self.results:
            icon = status_icon.get(result["status"], "❓")
            report += f"| {result['check']} | {icon} {result['status'].upper()} | {result['detail']} |\n"
        
        report += f"""
**汇总**：{passed} 项通过 / {warnings} 项警告 / {failed} 项失败 / {skipped} 项跳过

"""
        
        # 待确认清单
        todos = []
        for result in self.results:
            if result["status"] in ("warn", "fail"):
                if "missing" in result and result["missing"]:
                    todos.append(f"- [ ] **{result['check']}**：补充 {', '.join(result['missing'][:3])}")
                if "incomplete" in result and result["incomplete"]:
                    todos.append(f"- [ ] **{result['check']}**：完善 {', '.join(result['incomplete'][:2])}")
                if "issues" in result and result["issues"]:
                    todos.append(f"- [ ] **{result['check']}**：处理 {', '.join(result['issues'][:2])}")
                if "uncovered_count" in result and result["uncovered_count"] > 0:
                    todos.append(f"- [ ] **{result['check']}**：检查疑似遗漏的 {result['uncovered_count']} 个功能点")
        
        if todos:
            report += "### 待确认清单\n\n"
            report += "\n".join(todos[:10])  # 最多10条
            if len(todos) > 10:
                report += f"\n- [ ] ... 等共 {len(todos)} 项待处理"
            report += "\n"
        
        return report
    
    def print_console(self):
        """打印控制台报告"""
        print("=" * 60)
        print("  原型完整性验证报告")
        print("=" * 60)
        
        for result in self.results:
            status_color = {
                "pass": "\033[92m",   # 绿色
                "warn": "\033[93m",   # 黄色
                "fail": "\033[91m",   # 红色
                "skip": "\033[90m",   # 灰色
            }.get(result["status"], "\033[0m")
            
            reset = "\033[0m"
            print(f"\n{status_color}[{result['status'].upper()}]{reset} {result['check']}")
            print(f"      {result['detail']}")
        
        print("\n" + "=" * 60)
        
        passed = sum(1 for r in self.results if r["status"] == "pass")
        total = len(self.results)
        print(f"  结果：{passed}/{total} 项通过")
        print("=" * 60)


def main():
    if len(sys.argv) < 3:
        print("用法: python validate_prototype.py <prototype_path> <prd_path> [api_doc_path]")
        sys.exit(1)
    
    prototype_path = sys.argv[1]
    prd_path = sys.argv[2]
    api_doc_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    validator = PrototypeValidator(prototype_path, prd_path, api_doc_path)
    validator.run_all_checks()
    validator.print_console()
    
    # 同时输出 Markdown 报告到 stdout（可被重定向到文件）
    print("\n\n--- Markdown 报告 ---\n")
    print(validator.generate_report())


if __name__ == "__main__":
    main()
