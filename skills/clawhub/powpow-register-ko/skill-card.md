## Description:

PowPow 가입부터 이메일 인증, Alipay 또는 PayPal 구독 활성화, 원클릭 로그인까지 대화로 안내하고 필요한 단계를 대행합니다.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow에 가입하려는 사용자가 이메일 인증과 계정 생성, 구독 결제 페이지 이동 및 활성화 확인을 진행하도록 돕습니다. 결제 정보 입력은 사용자가 공식 결제 페이지에서 직접 완료합니다.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 이메일 인증번호와 임시 세션 토큰을 처리합니다.

Mitigation: 인증번호는 PowPow 가입에만 사용하고, 완료 후 임시 세션 상태를 정리합니다.

Risk: Alipay 또는 PayPal 결제 페이지를 열어 구독을 진행합니다.

Mitigation: 공식 결제 페이지인지 확인하고, 결제 자격증명 입력과 결제 승인은 사용자가 직접 수행합니다.

## Reference(s):

- [ClawHub 스킬 페이지](https://clawhub.ai/durenzidu/skills/powpow-register-ko)
- [PowPow 공식 사이트](https://global.powpow.online)
- [PowPow 가입 페이지](https://global.powpow.online/register)
- [PowPow 구독 페이지](https://global.powpow.online/subscription)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Markdown 대화 및 로그인·결제 페이지 링크]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [가입·구독 진행 상태와 후속 조치를 안내하며, 결제 자격증명은 수집하지 않습니다.]

## Skill Version(s):

2.1.0 (source: ClawHub release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
