## Description:

PowPow 가입과 이메일 인증, 구독 결제 주문 및 계정 활성화, 원클릭 로그인을 대화로 안내하고 지원합니다.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow에 가입하려는 사용자가 여행 일기를 지도에 게시하거나 디지털 휴먼과 대화할 수 있도록 계정을 만들고 구독을 활성화하는 과정을 돕습니다. 사용자는 이메일 인증번호를 확인하고 결제 화면에서 직접 결제합니다.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assistant handles a PowPow account password during signup and login refresh.

Mitigation: Pass the password through an environment variable rather than command-line arguments; do not retain or disclose it after use.

Risk: Temporary session tokens and generated login links can grant access to the new account.

Mitigation: Keep login links private and run cleanup when finished to remove temporary session state.

Risk: The assistant creates a payment order and opens an Alipay checkout page.

Mitigation: Have the user verify the checkout details and complete payment themselves; do not collect payment credentials.

## Reference(s):

- [PowPow 공식 사이트](https://global.powpow.online)
- [PowPow 가입 페이지](https://global.powpow.online/register)
- [PowPow 구독 페이지](https://global.powpow.online/subscription)
- [에이전트 가입 절차](references/agent-flow.md)
- [가입 및 오류 해결](references/registration-flow.md)
- [결제 및 계정 활성화](references/payment-and-activation.md)
- [제품 스크린샷 안내](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links, Images]

**Output Format:** [Markdown text with signup steps, optional product screenshots, and login or payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for assisted signup; falls back to guidance-only mode.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
