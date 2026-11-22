#!/usr/bin/env python3
"""Build the versioned yotta-resume security question bank."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
OUTPUT = SKILL_DIR / "data" / "question-bank.json"
GENERATED_AT = "2026-11-22"
BANK_VERSION = "0.2.0"
LEVELS = ("junior", "mid", "senior", "lead")


FAMILIES: dict[str, dict[str, Any]] = {
    "soc": {
        "short": "soc",
        "sources": ["nist-nice-2-2-0", "nist-csf-2-0", "mitre-attack-v18"],
        "boundary": "只讨论授权范围内的防御监测、分诊和验证，不提供未授权攻击步骤。",
        "topics": [
            ("告警分诊与优先级", "登录失败告警的上下文关联和资产优先级"),
            ("告警降噪", "重复告警降噪并验证漏报风险"),
            ("检测工程", "SIEM 规则调优、灰度和回滚"),
            ("端点检测", "EDR 告警分诊和隔离建议"),
            ("威胁情报", "情报命中的上下文验证和误报确认"),
            ("ATT&CK 映射", "技术映射、证据边界和置信度表达"),
            ("横向移动", "横向移动线索的验证和升级"),
            ("账号行为", "异常账号行为与权限使用核验"),
            ("恶意文件", "恶意文件告警的初筛和证据保全"),
            ("网络流量", "流量异常与业务基线的区分"),
            ("漏洞利用迹象", "漏洞告警与真实利用迹象的区分"),
            ("邮件安全", "邮件告警、用户影响范围和处置闭环"),
            ("云审计", "云审计日志异常的关联分析"),
            ("事件升级", "事件升级、值班交接和信息完整性"),
            ("队列治理", "告警队列积压和处置时效治理"),
            ("规则上线", "检测规则上线前的测试和回滚"),
            ("覆盖评估", "检测覆盖缺口和残余风险表达"),
            ("误报复核", "误报样本复核和知识沉淀"),
            ("运营指标", "SOC 运营指标和质量指标设计"),
            ("值班质量", "值班复盘、交接质量和持续改进"),
        ],
    },
    "incident_response": {
        "short": "ir",
        "sources": ["nist-csf-2-0", "nist-nice-2-2-0", "mitre-attack-v18"],
        "boundary": "只讨论授权事件响应、取证和恢复，不指导未授权入侵。",
        "topics": [
            ("事件分级", "事件分级和响应启动条件"),
            ("证据链", "证据保全、时间线和完整性校验"),
            ("主机隔离", "主机隔离决策和业务影响控制"),
            ("账号处置", "账号禁用、会话失效和恢复条件"),
            ("恶意进程", "恶意进程处置前后的证据顺序"),
            ("网络遏制", "网络遏制、分段和业务连续性"),
            ("勒索响应", "勒索事件的范围确认、隔离和恢复"),
            ("供应链事件", "供应链事件的依赖盘点和影响评估"),
            ("云凭证泄露", "云凭证泄露的失效、审计和影响核验"),
            ("数据泄露", "数据泄露事件的范围评估和证据边界"),
            ("取证镜像", "取证镜像、哈希校验和保管链"),
            ("日志留存", "日志留存、时钟一致性和证据链"),
            ("业务恢复", "业务恢复条件、验证和残余风险"),
            ("响应指标", "MTTD、MTTR 和处置质量复盘"),
            ("根因分析", "根因分析、纠正措施和复发防护"),
            ("指挥升级", "跨团队指挥、升级和风险决策"),
            ("外部通报", "外部通报、法务协作和披露边界"),
            ("对外沟通", "证据脱敏、事实口径和沟通审批"),
            ("演练设计", "桌面演练、评分锚点和改进闭环"),
            ("手册维护", "响应手册的变更、演练和版本治理"),
        ],
    },
    "offensive_security": {
        "short": "off",
        "sources": [
            "owasp-wstg",
            "owasp-top10-2025",
            "cwe-top25-2025",
            "nist-nice-2-2-0",
            "cisa-kev",
        ],
        "boundary": "只讨论已获明确授权的安全测试，不提供破坏性利用、绕过授权或批量攻击指令。",
        "topics": [
            ("授权边界", "授权书、测试范围和责任主体"),
            ("时间窗口", "测试时间窗、禁止动作和应急联系人"),
    ("资产确认", "网络边界、域名和合作方资产确认"),
            ("最小验证", "漏洞验证的最小影响和停止条件"),
            ("证据复现", "复现步骤、证据材料和可重复性"),
            ("数据风险", "可能写入业务数据时的风险闸门"),
            ("凭据处理", "凭据发现、脱敏和敏感信息保管"),
            ("横向验证", "横向移动验证的授权和影响边界"),
            ("权限提升", "权限提升验证的边界和证据要求"),
            ("持久化测试", "持久化测试的专项授权和清理计划"),
            ("后渗透证据", "后渗透阶段的证据保全和范围控制"),
            ("漏洞评级", "漏洞评级、业务影响和修复优先级"),
            ("报告撰写", "测试报告、复现证据和修复建议"),
            ("修复复测", "修复方案、复测范围和关闭条件"),
            ("高危沟通", "高危漏洞的应急沟通和升级路径"),
            ("环境差异", "测试环境与生产环境的差异说明"),
    ("组件风险", "外部组件、依赖和供应链风险"),
            ("攻击面", "供应链攻击面识别和授权确认"),
            ("扫描验证", "自动化扫描结果的人工验证"),
            ("红队复盘", "红队行动复盘、指标和经验沉淀"),
        ],
    },
    "appsec": {
        "short": "appsec",
        "sources": [
            "owasp-top10-2025",
            "owasp-wstg",
            "cwe-top25-2025",
            "nist-csf-2-0",
        ],
        "boundary": "只讨论自有代码和获授权应用的安全设计、验证和修复。",
        "topics": [
            ("威胁建模", "威胁建模的资产、参与者和信任边界"),
            ("数据流", "数据流、信任边界和攻击面表达"),
            ("身份认证", "身份认证设计和失败路径"),
            ("授权设计", "对象级授权、角色和越权防护"),
            ("注入防护", "输入处理、参数化和注入验证"),
            ("文件上传", "文件上传的校验、隔离和回滚"),
            ("反序列化", "反序列化风险识别和输入范围"),
            ("SSRF", "服务端请求伪造的网络边界控制"),
            ("密钥配置", "密钥、配置和敏感参数管理"),
            ("依赖安全", "依赖、构建和供应链安全"),
            ("SAST 分诊", "SAST 告警分诊和误报边界"),
            ("DAST 复现", "DAST 发现的人工复现和证据"),
            ("SCA 修复", "SCA 漏洞的修复优先级和升级条件"),
            ("SDLC 门禁", "安全需求和 SDLC 门禁设计"),
            ("代码审计", "代码审计范围、方法和证据"),
            ("修复兼容", "安全修复与接口兼容性的取舍"),
            ("需求验收", "安全需求的可测试验收条件"),
            ("漏洞回归", "漏洞回归、复测和关闭标准"),
            ("质量指标", "安全指标、逃逸率和质量趋势"),
            ("评审治理", "安全评审文化、例外和争议处理"),
        ],
    },
    "security_engineering": {
        "short": "seceng",
        "sources": [
            "nist-csf-2-0",
            "nist-nice-2-2-0",
            "cisa-kev",
            "mitre-attack-v18",
        ],
        "boundary": "只讨论获授权环境的防御加固、变更和验证。",
        "topics": [
            ("主机基线", "主机安全基线的控制目标和验证"),
            ("云 IAM", "云 IAM 最小权限和权限边界"),
            ("网络分段", "网络分段、访问控制和业务依赖"),
            ("日志采集", "日志采集、时间同步和完整覆盖"),
            ("端点部署", "端点检测的部署范围、策略和例外"),
            ("备份恢复", "备份、隔离和恢复演练"),
            ("补丁管理", "补丁分级、维护窗口和回滚"),
            ("密钥轮换", "密钥轮换、依赖方和失效顺序"),
            ("镜像安全", "容器镜像的构建、扫描和准入"),
            ("Kubernetes", "Kubernetes 基线、RBAC 和网络策略"),
            ("IaC 治理", "Terraform 变更、审查和漂移检测"),
            ("资产清单", "资产清单、归属和覆盖缺口"),
            ("暴露治理", "高危端口和暴露面治理"),
            ("配置漂移", "配置漂移检测、告警和修复"),
            ("灰度变更", "灰度变更、监控和回滚条件"),
            ("故障边界", "生产故障与安全事件的交接边界"),
            ("自动化脚本", "自动化脚本权限和误操作保护"),
            ("构建安全", "构建流水线和供应链控制"),
            ("监控有效性", "监控告警的有效性和盲区评估"),
            ("工程治理", "安全工程指标、SLO 和治理节奏"),
        ],
    },
    "grc_data_security": {
        "short": "grc",
        "sources": ["nist-csf-2-0", "nist-nice-2-2-0"],
        "boundary": "只讨论风险、控制和合规事实，不输出法律结论或替代正式审批。",
        "topics": [
            ("适用要求", "法规、标准和合同要求的适用性识别"),
            ("控制映射", "控制要求到技术和流程控制的映射"),
            ("风险评估", "风险场景、影响、可能性和证据"),
            ("风险接受", "残余风险、接受权限和复审"),
            ("供应商风险", "供应商依赖、评估和持续监控"),
            ("数据分级", "数据分类分级的依据和例外"),
            ("访问边界", "数据访问、最小权限和业务角色"),
            ("留存删除", "留存周期、删除请求和证明"),
            ("跨境事实", "跨境数据流、接收方和事实台账"),
            ("个人请求", "个人信息请求、身份核验和时限"),
            ("审计准备", "审计证据包和事实口径"),
            ("整改闭环", "审计发现、整改和复核证据"),
            ("例外管理", "控制例外、补偿控制和到期复审"),
            ("连续性依赖", "业务连续性和关键供应商依赖"),
            ("策略可执行", "安全策略的可执行性和责任"),
            ("责任矩阵", "组织角色、决策权和责任矩阵"),
            ("培训度量", "安全培训内容和有效性度量"),
            ("治理报告", "治理指标、董事会报告和决策依据"),
            ("变更跟踪", "法规、标准和合同变化的跟踪"),
            ("事件治理", "事件后的治理改进和控制更新"),
        ],
    },
}


LEVEL_STEMS = {
    "junior": "请解释“{topic}”的目标、基本步骤、常见误区和至少两项验证证据。",
    "mid": "请围绕“{topic}”给出一次真实项目中的处理流程，说明输入、关键判断、交付物、失败降级和复核证据。",
    "senior": "请设计一套覆盖“{topic}”的可验证方案，说明适用范围、风险取舍、监控指标、回滚条件和改进机制。",
    "lead": "如果由你负责“{topic}”的标准与治理，请说明职责分工、度量方式、例外审批、审计留痕和持续改进。",
}

LEVEL_EVIDENCE = {
    "junior": ["目标与边界", "基本步骤", "常见误区", "验证证据"],
    "mid": ["场景范围", "关键判断", "处理流程", "交付物", "失败降级", "复核证据"],
    "senior": ["适用范围", "风险取舍", "监控指标", "回滚条件", "验证证据", "改进机制"],
    "lead": ["职责分工", "度量方式", "例外审批", "审计留痕", "改进闭环", "决策依据"],
}

LEVEL_FOLLOWUPS = {
    "junior": "哪些结论不能只凭工具输出，需要人工确认？",
    "mid": "如果关键输入缺失，你会如何降级而不是猜测？",
    "senior": "如果监控指标改善但风险信号没有下降，你会如何调整方案？",
    "lead": "你如何证明例外项在到期前被重新评审？",
}


RESUME_FOLLOWUPS = {
    "soc": [
        ("告警处置规模", "请把简历里的告警处置经历改写成包含时间窗、告警规模、个人职责、研判方法和结果的证据句。", ["时间窗", "告警规模", "个人职责", "研判方法", "结果"]),
        ("误报治理", "请说明你实际参与过的一次误报治理：原规则、样本分层、改后效果和漏报复核证据。", ["原规则", "样本分层", "改后效果", "漏报复核"]),
        ("工具与规则", "请区分你使用过、配置过和独立设计过的 SIEM / EDR 能力，并各举一个证据。", ["工具范围", "配置范围", "设计责任", "证据"]),
        ("升级协作", "请说明一次你发现高风险线索后的升级对象、时间、证据和后续结果。", ["线索", "升级时间", "升级对象", "证据", "结果"]),
        ("运营复盘", "请说明一次值班复盘如何改变了规则、流程或团队协作，并给出可验证结果。", ["复盘问题", "改进动作", "责任边界", "验证结果"]),
    ],
    "incident_response": [
        ("事件时间线", "请说明一次应急事件的发现时间、确认时间、遏制时间和恢复时间，不能只写“及时处理”。", ["时间线", "事件类型", "个人职责", "遏制动作"]),
        ("证据保全", "请说明你在响应中保全了哪些证据、如何保证完整性，以及哪些细节已脱敏。", ["证据类型", "完整性方法", "保管链", "脱敏边界"]),
        ("遏制决策", "请说明一次隔离或断网决策的业务影响、批准人和回滚条件。", ["影响范围", "批准人", "遏制动作", "回滚条件"]),
        ("恢复验证", "请说明事件恢复后如何验证业务、安全和数据完整性，而不是只看服务恢复。", ["业务验证", "安全验证", "数据验证", "残余风险"]),
        ("整改闭环", "请把“完成复盘”改写成问题、根因、整改责任人、完成时间和复发验证证据。", ["问题", "根因", "责任人", "完成时间", "复发验证"]),
    ],
    "offensive_security": [
        ("授权范围", "请说明一次测试的授权主体、目标范围、时间窗、禁止动作和范围外资产处理方式。", ["授权主体", "目标范围", "时间窗", "禁止动作", "范围外处理"]),
        ("测试方法", "请区分你实际执行的验证方法和只阅读过的方法，并给出对应的测试记录。", ["个人执行", "方法", "测试记录", "证据边界"]),
        ("漏洞范围", "请把“发现多个高危漏洞”改写为漏洞类型、严重级别、影响范围、验证方式和修复状态。", ["漏洞类型", "严重级别", "影响范围", "验证方式", "修复状态"]),
        ("证据脱敏", "请说明哪些客户名、资产地址、漏洞编号或利用细节不能出现在简历中，如何脱敏。", ["敏感字段", "脱敏方式", "披露边界"]),
        ("修复复测", "请说明漏洞修复后的复测范围、复测结果和未能复测的原因。", ["复测范围", "复测结果", "未复测原因"]),
    ],
    "appsec": [
        ("应用范围", "请说明代码审计覆盖的应用、技术栈、代码规模和不在范围内的系统。", ["应用范围", "技术栈", "代码规模", "排除范围"]),
        ("审计方法", "请说明你实际使用的威胁建模、SAST、人工审计和动态验证方法及各自作用。", ["威胁建模", "SAST", "人工审计", "动态验证"]),
        ("漏洞类型", "请把“修复很多漏洞”改写为问题类型、风险等级、修复责任、修复率和统计时间窗。", ["问题类型", "风险等级", "修复责任", "修复率", "时间窗"]),
        ("复测证据", "请说明一个漏洞从发现到关闭的证据链，包括复现、修复、复测和关闭确认。", ["复现", "修复", "复测", "关闭确认"]),
        ("安全左移", "请说明你在需求、设计、开发或发布阶段实际推动过的一项安全机制及其效果。", ["阶段", "安全机制", "个人动作", "效果证据"]),
    ],
    "security_engineering": [
        ("环境规模", "请说明一次安全加固项目的环境、资产规模、覆盖范围和例外项。", ["环境", "资产规模", "覆盖范围", "例外项"]),
        ("控制目标", "请说明加固对应的控制目标、技术措施和业务约束，避免只列工具名称。", ["控制目标", "技术措施", "业务约束"]),
        ("变更回滚", "请说明一次安全变更的灰度范围、监控指标、回滚条件和实际操作结果。", ["灰度范围", "监控指标", "回滚条件", "结果"]),
        ("自动化", "请说明你编写的自动化脚本解决了什么风险、权限边界是什么、失败时如何保护环境。", ["风险", "脚本动作", "权限边界", "失败保护"]),
        ("验证证据", "请说明基线或加固结果如何验证，有哪些报告、看板或抽样结果可以佐证。", ["验证方法", "抽样结果", "报告或看板"]),
    ],
    "grc_data_security": [
        ("适用框架", "请说明一次风险或合规项目实际适用的框架、条款或控制要求，并区分事实与推断。", ["适用框架", "控制要求", "事实边界"]),
        ("控制范围", "请说明你负责的控制范围、排除范围和依赖团队，避免把团队成果写成本人主导。", ["控制范围", "排除范围", "依赖团队", "个人责任"]),
        ("整改闭环", "请说明一次整改从差距识别到关闭的证据链，包括责任人、期限和复核结果。", ["差距", "责任人", "期限", "复核结果"]),
        ("数据分级", "请说明一次数据分类分级项目的对象、分级依据、访问控制和遗留例外。", ["数据对象", "分级依据", "访问控制", "例外"]),
        ("残余风险", "请说明你如何记录残余风险、谁有权接受、如何复审，以及哪些结论不能由你单独给出。", ["残余风险", "接受权限", "复审周期", "结论边界"]),
    ],
}


SCENARIOS = {
    "soc": [
        ("误报治理", "某条高价值规则每天产生大量重复告警，但真实事件仍混在其中。请设计降噪验证方案，说明基线、样本分层、漏报复核和回滚条件。", ["基线", "样本分层", "漏报复核", "回滚条件"], "你如何证明告警数量下降不是靠放宽规则掩盖风险？"),
        ("跨源关联", "登录失败、EDR 告警和威胁情报同时命中同一资产。请说明分诊顺序、证据关联、升级条件和交接内容。", ["资产重要性", "跨源证据", "升级条件", "交接内容"], "如果资产归属未知，你会如何避免误判和越权操作？"),
    ],
    "incident_response": [
        ("遏制取舍", "一起疑似横向移动事件中，关键业务主机尚未确认失陷。请说明是否隔离、批准链、证据保全和恢复条件。", ["影响范围", "证据强度", "业务依赖", "批准链", "恢复条件"], "如果业务方要求立即恢复，你如何记录风险决策？"),
        ("云凭证泄露", "发现云访问密钥可能泄露，但尚不确定是否被使用。请设计失效、审计、影响评估和客户沟通流程。", ["失效顺序", "审计范围", "影响评估", "沟通边界"], "你如何区分密钥泄露事实与对业务影响的推断？"),
    ],
    "offensive_security": [
        ("最小验证", "你怀疑一个 Web 参数存在注入风险，但系统承载敏感业务。请说明最小验证、停止条件、证据保全和修复复测。", ["授权范围", "最小验证", "停止条件", "证据保全", "修复复测"], "如果验证可能写入业务数据，何时停止并申请专项确认？"),
        ("范围外资产", "测试中发现一个疑似关联域名但不在授权清单。请说明识别、隔离、报告和沟通流程。", ["授权清单", "范围判定", "停止动作", "报告对象"], "为什么不能把关联关系直接视为授权证据？"),
    ],
    "appsec": [
        ("风险上线", "上线前发现一个中危漏洞，修复会影响核心接口兼容性。请说明风险判断、补偿控制、批准链和复测计划。", ["业务影响", "可利用条件", "补偿控制", "批准链", "复测计划"], "你如何避免把风险接受写成漏洞已修复？"),
        ("依赖漏洞", "构建扫描发现高风险依赖漏洞，但升级会破坏旧接口。请说明修复优先级、隔离措施、兼容性验证和退出计划。", ["依赖范围", "可利用条件", "隔离措施", "兼容性验证", "退出计划"], "你如何证明临时隔离措施不会长期替代修复？"),
    ],
    "security_engineering": [
        ("IAM 收紧", "多租户云环境的 IAM 权限过宽。请设计灰度收紧、业务监控、异常场景和回滚条件。", ["权限差异", "灰度范围", "业务监控", "异常场景", "回滚条件"], "怎样证明收紧后没有产生新的越权路径？"),
        ("基线推广", "要在大量主机上推广新安全基线，同时存在遗留系统和业务例外。请设计分批、例外、验证和审计方案。", ["资产分层", "分批策略", "例外审批", "验证结果", "审计留痕"], "你如何防止例外项永久化？"),
    ],
    "grc_data_security": [
        ("新字段上线", "业务准备上线包含个人信息的新数据字段。请说明分类分级、访问角色、留存删除、跨境事实和审批边界。", ["数据字段", "分类分级", "访问角色", "留存删除", "跨境事实"], "哪些判断必须由法务、业务负责人或安全负责人确认？"),
        ("供应商审计", "关键供应商发生安全事件，但影响范围尚不明确。请说明事实核验、合同义务、风险隔离和复审计划。", ["事实核验", "合同义务", "风险隔离", "复审计划"], "你如何处理供应商声明与自有证据之间的冲突？"),
    ],
}


def canonical_hash(payload: dict[str, Any]) -> str:
    filtered = {key: value for key, value in payload.items() if key != "content_hash"}
    canonical = json.dumps(
        filtered,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def make_question(
    question_id: str,
    family: str,
    level: str,
    dimension: str,
    kind: str,
    prompt: str,
    expected_evidence: list[str],
    followups: list[str],
    source_refs: list[str],
    stale_after_days: int = 180,
) -> dict[str, Any]:
    question = {
        "question_id": question_id,
        "role_family": family,
        "level": level,
        "dimension": dimension,
        "kind": kind,
        "prompt": prompt,
        "expected_evidence": expected_evidence,
        "followups": followups,
        "answer_boundary": FAMILIES[family]["boundary"],
        "source_refs": source_refs,
        "status": "active",
        "last_verified_at": GENERATED_AT,
        "stale_after_days": stale_after_days,
        "freshness_label": "current",
    }
    question["content_hash"] = canonical_hash(question)
    return question


def build_bank() -> dict[str, Any]:
    questions: list[dict[str, Any]] = []
    for family, config in FAMILIES.items():
        short = config["short"]
        topics = config["topics"]
        if len(topics) != 20:
            raise ValueError(f"{family} must define 20 knowledge topics")

        for index, (dimension, topic) in enumerate(topics):
            level = LEVELS[index // 5]
            questions.append(
                make_question(
                    question_id=f"sec-{short}-knowledge-{index + 1:03d}",
                    family=family,
                    level=level,
                    dimension=dimension,
                    kind="knowledge",
                    prompt=LEVEL_STEMS[level].format(topic=topic),
                    expected_evidence=list(LEVEL_EVIDENCE[level]),
                    followups=[LEVEL_FOLLOWUPS[level]],
                    source_refs=list(config["sources"]),
                )
            )

        resume_items = RESUME_FOLLOWUPS[family]
        if len(resume_items) != 5:
            raise ValueError(f"{family} must define 5 resume followups")
        for index, (dimension, prompt, evidence) in enumerate(resume_items):
            level = ("junior", "mid", "mid", "senior", "lead")[index]
            questions.append(
                make_question(
                    question_id=f"sec-{short}-resume-{index + 1:03d}",
                    family=family,
                    level=level,
                    dimension=dimension,
                    kind="resume_followup",
                    prompt=prompt,
                    expected_evidence=evidence,
                    followups=["哪些数据尚未经你确认，不能写入简历？"],
                    source_refs=list(config["sources"][:2]),
                    stale_after_days=180,
                )
            )

        scenario_items = SCENARIOS[family]
        if len(scenario_items) != 2:
            raise ValueError(f"{family} must define 2 scenarios")
        for index, (dimension, prompt, evidence, followup) in enumerate(scenario_items):
            level = ("mid", "senior")[index]
            questions.append(
                make_question(
                    question_id=f"sec-{short}-scenario-{index + 1:03d}",
                    family=family,
                    level=level,
                    dimension=dimension,
                    kind="scenario",
                    prompt=prompt,
                    expected_evidence=evidence,
                    followups=[followup],
                    source_refs=list(config["sources"]),
                    stale_after_days=30 if family == "offensive_security" else 90,
                )
            )

    expected_total = len(FAMILIES) * (20 + 5 + 2)
    if len(questions) != expected_total:
        raise ValueError(f"expected {expected_total} questions, got {len(questions)}")

    ids = [item["question_id"] for item in questions]
    prompts = [item["prompt"] for item in questions]
    if len(ids) != len(set(ids)):
        raise ValueError("question IDs must be unique")
    if len(prompts) != len(set(prompts)):
        raise ValueError("question prompts must be unique")

    return {
        "schema_version": "1.0",
        "contract_version": "1.0",
        "bank_version": BANK_VERSION,
        "generated_at": GENERATED_AT,
        "questions": questions,
    }


def render_bank() -> bytes:
    return (
        json.dumps(build_bank(), ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    rendered = render_bank()
    if args.write:
        OUTPUT.write_bytes(rendered)
        return 0

    if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
        print(f"question bank is stale: {OUTPUT}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
