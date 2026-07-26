#!/usr/bin/env python3
"""
PIPL Compliance Checker — 中国个人信息保护法合规检查工具

内嵌合规检查核心模块，提供标准化的 CLI、报告输出和检查引擎。
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))  # scripts/ directory

try:
    from core import UnifiedCLI, CheckEngine, CheckResult, Severity
except ImportError as e:
    print(f"[ERROR] 核心模块加载失败: {e}", file=sys.stderr)
    print("[ERROR] 请确保 scripts/core/ 目录完整。如依赖缺失请运行: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)



class PIPLChecker(CheckEngine):
    """PIPL 合规检查引擎"""

    def __init__(self):
        super().__init__(
            tool_name="PIPL-Compliance",
            regulation="Personal Information Protection Law (个人信息保护法)"
        )
        self._register_all()

    def _register_all(self):
        """注册所有检查项和场景"""

        self.register_checker("consent", self._check_consent)
        self.register_checker("notification", self._check_notification)
        self.register_checker("minimization", self._check_minimization)
        self.register_checker("security", self._check_security)
        self.register_checker("individual_rights", self._check_rights)
        self.register_checker("cross_border", self._check_cross_border)
        self.register_checker("sensitive_info", self._check_sensitive_info)
        self.register_checker("automated_decision", self._check_automated_decision)
        self.register_checker("third_party", self._check_third_party)
        self.register_checker("data_impact", self._check_data_impact)
        self.register_checker("breach_notification", self._check_breach)
        self.register_checker("delegated_processing", self._check_delegated)
        self.register_checker("rights_mechanism", self._check_rights_mechanism)
        self.register_checker("merger_transfer", self._check_merger_transfer)
        self.register_checker("public_disclosure", self._check_public_disclosure)
        self.register_checker("public_space_device", self._check_public_space_device)
        self.register_checker("public_data", self._check_public_data)
        self.register_checker("minors", self._check_minors)
        self.register_checker("rights_response", self._check_rights_response)
        self.register_checker("internal_management", self._check_internal_management)

        self.register_scenario("user_registration", "用户注册场景",
            ["consent", "notification", "minimization", "security"])
        self.register_scenario("location_collection", "位置信息收集",
            ["consent", "notification", "minimization", "security", "sensitive_info"],
            description="含单独同意要求")
        self.register_scenario("marketing_push", "营销推送",
            ["consent", "notification", "minimization", "individual_rights"])
        self.register_scenario("cross_border_transfer", "跨境数据传输",
            ["consent", "notification", "cross_border", "security", "data_impact"])
        self.register_scenario("sensitive_data", "敏感信息处理",
            ["consent", "notification", "sensitive_info", "security", "minimization"],
            description="含单独同意+额外安全保障")
        self.register_scenario("full_audit", "全面审计",
            ["consent", "notification", "minimization", "security",
             "individual_rights", "cross_border", "sensitive_info",
             "automated_decision", "third_party", "data_impact",
             "breach_notification", "delegated_processing",
             "rights_mechanism", "merger_transfer", "public_disclosure",
             "public_space_device", "public_data", "minors",
             "rights_response", "internal_management"])

        # === 《小型个人信息处理者个人信息保护简化措施规定》(2026-09-01) 19项审计框架 ===
        self.register_scenario("small_processor_audit", "小型个人信息处理者合规审计",
            ["consent",              # 1. 合法性基础
             "notification",         # 2. 处理规则
             "rights_mechanism",     # 3. 权益保障机制
             "delegated_processing", # 4. 委托处理
             "merger_transfer",      # 5. 合并重组转移
             "third_party",          # 6/7. 向其他处理者提供
             "automated_decision",   # 8. 自动化决策
             "public_disclosure",    # 9. 公开个人信息
             "public_space_device",  # 10. 公共场所设备
             "public_data",          # 11. 已公开信息
             "sensitive_info",       # 12. 敏感信息
             "minors",              # 13. 未成年人
             "cross_border",        # 14. 跨境传输
             "individual_rights",   # 15/16. 删除权/个人权利
             "rights_response",     # 17. 响应权利申请
             "internal_management", # 18. 内部管理制度
             "security"],           # 19. 技术措施
            description="依据《小型个人信息处理者个人信息保护简化措施规定》附件1的19项审计事项")

    def _check_consent(self, data: dict) -> CheckResult:
        """检查用户同意机制"""
        has_consent = data.get("has_consent", False)
        is_informed = data.get("is_informed", False)
        is_voluntary = data.get("is_voluntary", False)
        can_withdraw = data.get("can_withdraw", False)
        separate_consent = data.get("separate_consent", data.get("敏感信息", False))

        issues = []
        if not has_consent: issues.append("未获得用户同意")
        if not is_informed: issues.append("未确保用户在充分知情下同意")
        if not is_voluntary: issues.append("存在捆绑同意问题")
        if not can_withdraw: issues.append("未提供撤回同意的便捷方式")
        if separate_consent and not data.get("has_separate_consent", False):
            issues.append("处理敏感信息未取得单独同意")

        return CheckResult(
            check_id="consent",
            description="用户同意机制检查",
            severity=Severity.FAIL if not has_consent else Severity.WARN,
            passed=has_consent and is_informed and can_withdraw,
            details="；".join(issues) if issues else "同意机制合规",
            recommendation="取得用户真实意愿的同意，提供便捷的撤回方式",
            regulation_ref="PIPL Art.14-16"
        )

    def _check_notification(self, data: dict) -> CheckResult:
        """检查告知义务"""
        has_notice = data.get("has_notice", False)
        has_identity = data.get("has_identity", False)
        has_purpose = data.get("has_purpose", False)
        has_method = data.get("has_method", False)
        has_retention = data.get("has_retention", False)
        has_rights = data.get("has_rights", False)

        missing = []
        if not has_notice: missing.append("未制定告知规则")
        if not has_identity: missing.append("未告知处理者身份")
        if not has_purpose: missing.append("未告知处理目的和方式")
        if not has_method: missing.append("未告知处理的个人信息种类和保存期限")
        if not has_rights: missing.append("未告知个人行使权利的方式和程序")

        return CheckResult(
            check_id="notification",
            description="告知义务检查",
            severity=Severity.FAIL if not has_notice else Severity.PASS,
            passed=len(missing) == 0,
            details="缺失: " + "、".join(missing) if missing else "告知义务履行完整",
            recommendation="制定清晰的个人信息处理规则，以显著方式告知",
            regulation_ref="PIPL Art.17"
        )

    def _check_minimization(self, data: dict) -> CheckResult:
        """检查数据最小化"""
        has_clear_purpose = data.get("has_clear_purpose", False)
        is_minimal = data.get("is_minimal", False)
        not_excessive = data.get("not_excessive", False)

        issues = []
        if not has_clear_purpose: issues.append("处理目的不明确")
        if not is_minimal: issues.append("数据收集超出最小必要范围")
        if not not_excessive: issues.append("数据处理超出实现目的所需")

        return CheckResult(
            check_id="minimization",
            description="数据最小化原则检查",
            severity=Severity.FAIL if not is_minimal else Severity.PASS,
            passed=has_clear_purpose and is_minimal and not_excessive,
            details="；".join(issues) if issues else "数据最小化原则合规",
            recommendation="遵循最小必要原则，仅收集与目的直接相关的个人信息",
            regulation_ref="PIPL Art.6"
        )

    def _check_security(self, data: dict) -> CheckResult:
        """检查安全保障措施"""
        has_classification = data.get("has_classification", False)
        has_encryption = data.get("has_encryption", False)
        has_access_control = data.get("has_access_control", False)
        has_emergency = data.get("has_emergency", False)
        has_training = data.get("has_training", False)

        issues = []
        if not has_classification: issues.append("未实施个人信息分类管理")
        if not has_encryption: issues.append("未采取加密措施")
        if not has_access_control: issues.append("访问控制不足")
        if not has_emergency: issues.append("无应急响应预案")

        return CheckResult(
            check_id="security",
            description="安全保障措施检查",
            severity=Severity.FAIL if not has_encryption else Severity.WARN,
            passed=has_classification and has_encryption and has_access_control,
            details="；".join(issues) if issues else "安全保障措施完善",
            recommendation="实施分类管理、加密、访问控制、应急响应等安全措施",
            regulation_ref="PIPL Art.51-53"
        )

    def _check_rights(self, data: dict) -> CheckResult:
        """检查个人权利保障"""
        has_knowledge = data.get("has_knowledge", False)
        has_decision = data.get("has_decision", False)
        has_deletion = data.get("has_deletion", False)
        has_correction = data.get("has_correction", False)
        has_copy = data.get("has_copy", False)

        missing = []
        if not has_knowledge: missing.append("查阅权")
        if not has_correction: missing.append("更正权")
        if not has_deletion: missing.append("删除权")
        if not has_copy: missing.append("复制权")

        return CheckResult(
            check_id="individual_rights",
            description="个人在信息处理活动中的权利检查",
            severity=Severity.FAIL if len(missing) > 0 else Severity.PASS,
            passed=len(missing) == 0,
            details="缺失: " + "、".join(missing) if missing else "个人权利保障完整",
            recommendation="建立便捷的个人权利请求处理机制",
            regulation_ref="PIPL Art.44-50"
        )

    def _check_cross_border(self, data: dict) -> CheckResult:
        """检查跨境传输合规"""
        transfers_abroad = data.get("transfers_abroad", False)
        has_security_assessment = data.get("has_security_assessment", False)
        has_certification = data.get("has_certification", False)
        has_contract = data.get("has_contract", False)
        has_informed_consent = data.get("has_informed_consent", False)

        issues = []
        if transfers_abroad:
            if not has_security_assessment:
                issues.append("未通过安全评估")
            if not has_certification and not has_contract:
                issues.append("未经专业机构认证或未订立标准合同")
            if not has_informed_consent:
                issues.append("未告知境外接收方信息并取得单独同意")

        return CheckResult(
            check_id="cross_border",
            description="跨境数据传输合规检查",
            severity=Severity.FAIL if transfers_abroad and not has_security_assessment else Severity.WARN,
            passed=not transfers_abroad or (has_security_assessment and has_informed_consent),
            details="；".join(issues) if issues else "跨境传输合规",
            recommendation="完成安全评估、认证或签订标准合同，取得单独同意",
            regulation_ref="PIPL Art.38-43"
        )

    def _check_sensitive_info(self, data: dict) -> CheckResult:
        """检查敏感个人信息处理"""
        processes_sensitive = data.get("processes_sensitive", False)
        has_specific_purpose = data.get("has_specific_purpose", False)
        has_separate_consent = data.get("has_separate_consent", False)
        has_necessity = data.get("has_necessity", False)
        has_impact_assessment = data.get("has_impact_assessment", False)

        if not processes_sensitive:
            return CheckResult("sensitive_info", "敏感信息处理检查",
                Severity.PASS, True, "未处理敏感个人信息", regulation_ref="PIPL Art.28-32")

        issues = []
        if not has_specific_purpose: issues.append("未明确特定目的")
        if not has_separate_consent: issues.append("未取得单独同意")
        if not has_necessity: issues.append("无充分必要性说明")
        if not has_impact_assessment: issues.append("未进行影响评估")

        return CheckResult(
            check_id="sensitive_info",
            description="敏感个人信息处理合规检查",
            severity=Severity.FAIL if not has_separate_consent else Severity.FAIL,
            passed=has_specific_purpose and has_separate_consent and has_impact_assessment,
            details="；".join(issues) if issues else "敏感信息处理合规",
            recommendation="取得单独同意，进行影响评估，采取严格保护措施",
            regulation_ref="PIPL Art.28-32"
        )

    def _check_automated_decision(self, data: dict) -> CheckResult:
        """检查自动化决策"""
        uses_automated = data.get("uses_automated", False)
        has_transparency = data.get("has_transparency", False)
        offers_opt_out = data.get("offers_opt_out", False)

        if not uses_automated:
            return CheckResult("automated_decision", "自动化决策合规检查",
                Severity.PASS, True, "未使用自动化决策")

        issues = []
        if not has_transparency: issues.append("未说明自动化决策方式和结果")
        if not offers_opt_out: issues.append("未提供拒绝仅通过自动化决策的权利")

        return CheckResult(
            check_id="automated_decision",
            description="自动化决策合规检查",
            severity=Severity.FAIL if not offers_opt_out else Severity.PASS,
            passed=has_transparency and offers_opt_out,
            details="；".join(issues) if issues else "自动化决策合规",
            recommendation="保证决策透明度和结果公平公正，提供拒绝权",
            regulation_ref="PIPL Art.24"
        )

    def _check_third_party(self, data: dict) -> CheckResult:
        """检查第三方共享"""
        shares_with_third = data.get("shares_with_third", False)
        has_notice = data.get("has_notice", False)
        has_informed_consent = data.get("has_informed_consent", False)
        has_contract = data.get("has_contract", False)

        if not shares_with_third:
            return CheckResult("third_party", "第三方共享检查",
                Severity.PASS, True, "未向第三方提供个人信息")

        issues = []
        if not has_notice: issues.append("未告知接收方信息")
        if not has_informed_consent: issues.append("未取得单独同意")
        if not has_contract: issues.append("未订立合同明确权责")

        return CheckResult(
            check_id="third_party",
            description="向第三方提供个人信息检查",
            severity=Severity.FAIL if not has_informed_consent else Severity.PASS,
            passed=has_notice and has_informed_consent and has_contract,
            details="；".join(issues) if issues else "第三方共享合规",
            recommendation="告知接收方信息、取得单独同意、签订合同明确责任",
            regulation_ref="PIPL Art.21-23"
        )

    def _check_data_impact(self, data: dict) -> CheckResult:
        """检查影响评估"""
        high_risk = data.get("high_risk", False)
        has_assessment = data.get("has_assessment", False)
        assessment_complete = data.get("assessment_complete", False)

        if not high_risk:
            return CheckResult("data_impact", "个人信息保护影响评估检查",
                Severity.PASS, True, "无需进行影响评估")

        issues = []
        if not has_assessment: issues.append("高风险处理但未进行影响评估")
        if has_assessment and not assessment_complete: issues.append("影响评估不完整")

        return CheckResult(
            check_id="data_impact",
            description="个人信息保护影响评估检查",
            severity=Severity.FAIL if not has_assessment else Severity.PASS,
            passed=has_assessment and assessment_complete,
            details="；".join(issues) if issues else "影响评估完整",
            recommendation="对高风险处理活动进行个人信息保护影响评估",
            regulation_ref="PIPL Art.55-56"
        )

    def _check_breach(self, data: dict) -> CheckResult:
        """检查泄露通知义务"""
        has_response_plan = data.get("has_response_plan", False)
        notifies_regulator = data.get("notifies_regulator", False)
        notifies_individuals = data.get("notifies_individuals", False)

        issues = []
        if not has_response_plan: issues.append("无安全事件应急响应计划")
        if not notifies_regulator: issues.append("未建立向监管部门的通知机制")
        if not notifies_individuals: issues.append("未建立向个人的通知机制")

        return CheckResult(
            check_id="breach_notification",
            description="个人信息泄露通知义务检查",
            severity=Severity.FAIL if not has_response_plan else Severity.WARN,
            passed=has_response_plan and notifies_regulator,
            details="；".join(issues) if issues else "通知机制完善",
            recommendation="建立应急响应计划并通知监管和个人",
            regulation_ref="PIPL Art.57"
        )

    def _check_delegated(self, data: dict) -> CheckResult:
        """检查委托处理"""
        has_delegated = data.get("has_delegated", False)
        has_agreement = data.get("has_agreement", False)
        has_supervision = data.get("has_supervision", False)

        if not has_delegated:
            return CheckResult("delegated_processing", "委托处理检查",
                Severity.PASS, True, "无委托处理活动")

        issues = []
        if not has_agreement: issues.append("未订立委托处理协议")
        if not has_supervision: issues.append("未对受托方进行监督")

        return CheckResult(
            check_id="delegated_processing",
            description="委托处理个人信息合规检查",
            severity=Severity.FAIL if not has_agreement else Severity.PASS,
            passed=has_agreement and has_supervision,
            details="；".join(issues) if issues else "委托处理合规",
            recommendation="订立委托处理协议并监督受托方的处理活动",
            regulation_ref="PIPL Art.21"
        )

    # ── 新增检查器：依据《小型个人信息处理者个人信息保护简化措施规定》(2026-09-01) 附件1 ──

    def _check_rights_mechanism(self, data: dict) -> CheckResult:
        """3. 个人信息保护权益保障机制"""
        has_clear_rights = data.get("has_clear_rights", False)
        has_complaint = data.get("has_complaint", False)
        has_response_procedure = data.get("has_response_procedure", False)
        has_deletion_mechanism = data.get("has_deletion_mechanism", False)

        issues = []
        if not has_clear_rights: issues.append("未明确告知个人权益")
        if not has_complaint: issues.append("未建立投诉举报渠道")
        if not has_response_procedure: issues.append("未建立权利响应流程")

        return CheckResult(
            check_id="rights_mechanism",
            description="个人信息保护权益保障机制检查",
            severity=Severity.FAIL if not has_response_procedure else Severity.PASS,
            passed=has_clear_rights and has_complaint and has_response_procedure,
            details="；".join(issues) if issues else "权益保障机制完整",
            recommendation="明确告知权益、建立投诉渠道和权利响应流程",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第3项"
        )

    def _check_merger_transfer(self, data: dict) -> CheckResult:
        """5. 合并、重组、解散等原因转移个人信息"""
        has_merger_scenario = data.get("has_merger_scenario", False)
        notifies_individual = data.get("notifies_individual", False)
        has_receiver_info = data.get("has_receiver_info", False)

        if not has_merger_scenario:
            return CheckResult("merger_transfer", "合并重组转移个人信息检查",
                Severity.PASS, True, "无合并重组等转移个人信息的情形",
                regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第5项")

        issues = []
        if not notifies_individual: issues.append("未向个人告知转移事项")
        if not has_receiver_info: issues.append("未告知接收方名称或联系方式")

        return CheckResult(
            check_id="merger_transfer",
            description="合并重组转移个人信息检查",
            severity=Severity.FAIL if not notifies_individual else Severity.PASS,
            passed=notifies_individual and has_receiver_info,
            details="；".join(issues) if issues else "转移通知合规",
            recommendation="向个人告知接收方名称或姓名和联系方式",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第5项；PIPL Art.22"
        )

    def _check_public_disclosure(self, data: dict) -> CheckResult:
        """9. 基于个人同意公开个人信息"""
        discloses_publicly = data.get("discloses_publicly", False)
        has_separate_consent = data.get("has_separate_consent", False)
        has_impact_assessment = data.get("has_impact_assessment", False)

        if not discloses_publicly:
            return CheckResult("public_disclosure", "公开个人信息检查",
                Severity.PASS, True, "未公开处理个人信息",
                regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第9项")

        issues = []
        if not has_separate_consent: issues.append("未取得个人单独同意")
        if not has_impact_assessment: issues.append("公开前未进行个人信息保护影响评估")

        return CheckResult(
            check_id="public_disclosure",
            description="公开个人信息合规检查",
            severity=Severity.FAIL if not has_separate_consent else Severity.PASS,
            passed=has_separate_consent and has_impact_assessment,
            details="；".join(issues) if issues else "公开个人信息合规",
            recommendation="取得个人单独同意，事前进行个人信息保护影响评估",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第9项；PIPL Art.25"
        )

    def _check_public_space_device(self, data: dict) -> CheckResult:
        """10. 公共场所图像收集、个人身份识别设备"""
        has_public_device = data.get("has_public_device", False)
        is_public_safety = data.get("is_public_safety", False)
        has_prominent_sign = data.get("has_prominent_sign", False)
        has_separate_consent_commercial = data.get("has_separate_consent_commercial", False)

        if not has_public_device:
            return CheckResult("public_space_device", "公共场所设备检查",
                Severity.PASS, True, "未在公共场所安装图像/身份识别设备",
                regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第10项")

        issues = []
        if not is_public_safety: issues.append("非公共安全所必需")
        if not has_prominent_sign: issues.append("未设置显著提示标识")
        if not has_separate_consent_commercial:
            issues.append("用于维护公共安全以外用途未取得单独同意")

        return CheckResult(
            check_id="public_space_device",
            description="公共场所图像/身份识别设备检查",
            severity=Severity.FAIL if not is_public_safety else Severity.WARN,
            passed=is_public_safety and has_prominent_sign and has_separate_consent_commercial,
            details="；".join(issues) if issues else "公共场所设备合规",
            recommendation="确认为公共安全所必需、设置显著提示标识、商业用途需单独同意",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第10项；PIPL Art.26"
        )

    def _check_public_data(self, data: dict) -> CheckResult:
        """11. 处理已公开的个人信息"""
        processes_public = data.get("processes_public", False)
        not_send_unauthorized = data.get("not_send_unauthorized", False)
        not_cyber_violence = data.get("not_cyber_violence", False)
        respects_refusal = data.get("respects_refusal", False)

        if not processes_public:
            return CheckResult("public_data", "已公开个人信息处理检查",
                Severity.PASS, True, "未处理已公开个人信息",
                regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第11项")

        issues = []
        if not not_send_unauthorized: issues.append("向已公开信息中的邮箱/手机号发送无关商业信息")
        if not not_cyber_violence: issues.append("利用已公开信息从事网络暴力或传播谣言")
        if not respects_refusal: issues.append("处理个人明确拒绝的已公开信息")

        return CheckResult(
            check_id="public_data",
            description="已公开个人信息处理检查",
            severity=Severity.FAIL if not not_cyber_violence else Severity.WARN,
            passed=not_send_unauthorized and not_cyber_violence and respects_refusal,
            details="；".join(issues) if issues else "已公开信息处理合规",
            recommendation="不得发送无关商业信息、不得从事网络暴力、尊重个人拒绝权",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第11项；PIPL Art.27"
        )

    def _check_minors(self, data: dict) -> CheckResult:
        """13. 未成年人个人信息保护"""
        processes_minors = data.get("processes_minors", False)
        has_parental_consent = data.get("has_parental_consent", False)
        has_minor_policy = data.get("has_minor_policy", False)
        not_force_nonessential = data.get("not_force_nonessential", False)

        if not processes_minors:
            return CheckResult("minors", "未成年人信息保护检查",
                Severity.PASS, True, "不处理未成年人个人信息",
                regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第13项")

        issues = []
        if not has_parental_consent: issues.append("处理未满14周岁未成年人信息未取得监护人同意")
        if not has_minor_policy: issues.append("未制定专门的未成年人信息处理规则")
        if not not_force_nonessential: issues.append("强制要求同意非必要信息")

        return CheckResult(
            check_id="minors",
            description="未成年人个人信息保护检查",
            severity=Severity.FAIL if not has_parental_consent else Severity.PASS,
            passed=has_parental_consent and has_minor_policy,
            details="；".join(issues) if issues else "未成年人保护合规",
            recommendation="取得监护人同意、制定专门规则、不强制同意非必要信息",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第13项；PIPL Art.31"
        )

    def _check_rights_response(self, data: dict) -> CheckResult:
        """17. 响应个人行使权利申请"""
        has_acceptance_mechanism = data.get("has_acceptance_mechanism", False)
        responds_in_time = data.get("responds_in_time", False)
        provides_explanation = data.get("provides_explanation", False)
        explains_refusal = data.get("explains_refusal", False)

        issues = []
        if not has_acceptance_mechanism: issues.append("未提供便捷的申请受理机制")
        if not responds_in_time: issues.append("未及时响应个人权利申请")
        if not provides_explanation: issues.append("未用通俗易懂语言解释处理规则")
        if not explains_refusal: issues.append("拒绝请求时未说明理由")

        return CheckResult(
            check_id="rights_response",
            description="响应个人行使权利申请检查",
            severity=Severity.FAIL if not has_acceptance_mechanism else Severity.PASS,
            passed=has_acceptance_mechanism and responds_in_time,
            details="；".join(issues) if issues else "权利响应机制完善",
            recommendation="建立便捷受理机制、及时响应、拒绝时说明理由",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第17项；PIPL Art.48-49"
        )

    def _check_internal_management(self, data: dict) -> CheckResult:
        """18. 内部管理制度和操作规程"""
        has_policy = data.get("has_policy", False)
        has_org_structure = data.get("has_org_structure", False)
        has_classification = data.get("has_classification", False)
        has_emergency_plan = data.get("has_emergency_plan", False)
        has_audit_system = data.get("has_audit_system", False)
        has_training = data.get("has_training", False)
        has_access_control = data.get("has_access_control", False)
        has_dpo = data.get("has_dpo", False)

        issues = []
        if not has_policy: issues.append("未制定个人信息保护方针目标")
        if not has_org_structure: issues.append("未建立保护组织架构")
        if not has_classification: issues.append("未实施个人信息分类")
        if not has_emergency_plan: issues.append("未建立安全事件应急响应机制")
        if not has_audit_system: issues.append("未建立合规审计制度")
        if not has_training: issues.append("未实施安全教育和培训")
        if not has_access_control: issues.append("未合理制定操作权限")
        if not has_dpo and data.get("requires_dpo", False):
            issues.append("应指定个人信息保护负责人但未指定")

        return CheckResult(
            check_id="internal_management",
            description="内部管理制度和操作规程检查",
            severity=Severity.FAIL if len(issues) > 3 else Severity.WARN,
            passed=has_policy and has_org_structure and has_emergency_plan,
            details="；".join(issues) if issues else "内部管理制度完善",
            recommendation="建立覆盖组织架构、分类管理、应急响应、培训审计的完整制度体系",
            regulation_ref="《小型个人信息处理者个人信息保护简化措施规定》附件1第18项；PIPL Art.51-52"
        )



def main():
    engine = PIPLChecker()
    cli = UnifiedCLI(
        tool_name="pipl-check.py",
        description="PIPL合规检查工具 — 中国个人信息保护法合规评估"
    )
    args = cli.parse_args()

    if args.list_scenarios:
        cli.list_scenarios(engine.get_scenarios())
        return

    report = engine.run(
        scenario=args.scenario,
        interactive=args.interactive,
    )

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            if args.format == "json":
                import json
                json.dump(report.to_dict(), f, indent=2, ensure_ascii=False)
            elif args.format == "markdown":
                from core.report_core import ReportGenerator
                f.write(ReportGenerator.to_markdown(report.to_dict()))
            else:
                f.write(str(report.to_dict()))
        print(f"\n✅ 报告已保存到: {args.output}")

    cli.print_report(report, fmt=args.format)


if __name__ == "__main__":
    main()
