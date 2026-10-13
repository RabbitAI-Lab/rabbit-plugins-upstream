# Agent 대행 플로우와 스크립트 계약 — powpow-register

SKILL.md 각 단계의 실행 세부사항. 모든 커맨드는 `node scripts/powpow-register.mjs <서브커맨드> [인자]` 형식이며,
스크립트는 **의존성 제로**, **Node ≥ 18** 필요. 모든 요청은 `https://global.powpow.online`로만 전송됩니다.

## 보안 설계(왜 이렇게 설계했는가)

| 설계 | 이유 |
|---|---|
| 비밀번호는 환경변수 `POWPOW_REGISTER_PASSWORD`로만 전달 | 프로세스의 커맨드라인 인자는 같은 컴퓨터의 다른 프로세스에서 보입니다(argv 유출면). 환경변수는 스크립트 안에서 읽자마자 사용 |
| 비밀번호는 **상태 파일에 절대 쓰지 않고** 로그에도 남기지 않음 | 상태 파일은 디스크에 남을 수 있음. 대화에서 생성 모드가 한 번만 표시하는 건 사용자가 저장하게 하기 위한 것 |
| 상태 파일은 시스템 임시 디렉터리에 저장(`os.tmpdir()/powpow-register-state.json`, 0600) | email / username / nickname / token / outTradeNo 다섯 필드만 포함. `cleanup`으로 한 번에 삭제 |
| agent가 받은 JWT는 공식 `me?token=` 엔드포인트를 통해 브라우저 cookie로 교환 | 플랫폼이 HarmonyOS WebView용으로 설계한 공식 브리지. 검증은 서명+유효기간만 확인하고 기기 지문에 묶이지 않아 사용자 브라우저에서 사용 가능 |
| 결제는 create-order / query / 계산대 열기만 | 결제 행위와 결제 자격증명은 항상 사용자와 Alipay 공식 계산대 사이에 있으며 agent는 경유하지 않음 |

## 커맨드 레퍼런스

| 커맨드 | 주요 인자 | 역할 / 시점 |
|---|---|---|
| `status` | —— | 플로우 진행 확인(상태 파일 읽기). 대화 중단 후엔 먼저 이것 실행 |
| `gen-password` | —— | 24자리 강력 비밀번호 생성(대소문자+숫자 포함). stdout 표시는 **이때 한 번뿐** |
| `prepare-suggest` | `--username --nickname --email` | 확인된 정보를 상태 파일에 기록(이후 register에서 재입력 불필요) |
| `send-code` | `--email` | 플랫폼에 6자리 인증번호 발송 트리거(10분 유효, 60초 쿨다운) |
| `register` | `--code`(필수); `--username --nickname --avatar --phone`(선택, 상태 파일에 있으면 생략 가능) | pending 계정 생성. 비밀번호는 `POWPOW_REGISTER_PASSWORD` 환경변수로 전달. 성공 후 JWT는 자동으로 상태 파일에 저장 |
| `login-link` | `--target pending` 또는 `--target home` | 원클릭 로그인 링크 생성(더블 링크 설계, 아래 참조) |
| `create-order` | `--package monthly\|quarterly\|yearly`(Alipay 기본값)<br>`--provider alipay\|paypal` | 결제 주문 생성. Alipay는 결제 페이지 파일 경로 + outTradeNo, PayPal은 승인 페이지 파일 경로 + subscriptionId 반환(자동으로 상태 파일에 기록) |
| `query` | —— | 주문/구독 상태 조회. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`. 10~15초 간격 폴링 |
| `refresh-login` | 비밀번호는 환경변수로 | 재로그인으로 **새 JWT**로 교환(구독 클레임이 NONE → ACTIVE). 결제 입금 후 반드시 실행 |
| `whoami` | —— | 상태 파일의 token으로 계정과 구독 상태 조회(활성화가 적용됐는지 검증) |
| `cleanup` | —— | 상태 파일 삭제(마무리에서 반드시 실행) |

**환경변수 전달**(비밀번호는 절대 커맨드라인에 올리지 않음):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<비밀번호>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<비밀번호>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<비밀번호> && node scripts/powpow-register.mjs register --code 123456
```

## 더블 링크 메커니즘(핵심 설계)

플랫폼 로그인 상태는 HttpOnly cookie라서, agent가 브라우저에 직접 cookie를 심을 수 없습니다. 브리지는 공식
`/api/auth/me?token=<JWT>&redirect=<사이트 내 경로>` 엔드포인트: 서명 검증 → pending 사용자에게 자동으로 session 보완 생성 → `Set-Cookie: powpow_token`(HttpOnly / SameSite=Lax / 7일) → redirect 검증(단일 슬래시 시작만 허용, `//`와 백슬래시 금지, 파싱 후 동일 출처여야 함) → 307 임시 리다이렉트로 대상 페이지로.

- **링크 1(가입 성공 직후 줌)**: `--target pending` → `/subscription` 도착.
  사용자 브라우저는 '하프 로그인' 상태가 됩니다: 구독 페이지, Alipay 회귀 페이지는 보고 조작 가능. 콘텐츠 페이지는 여전히 페이월에 막혀 구독 페이지로 튕깁니다(3층 방어: JWT claims 게이트웨이 검사 → DB 재검사 → 코어 API 검사. 정상 동작입니다).
- **링크 2(paid 확인 후 줌)**: 먼저 `refresh-login`으로 새 JWT 교체(결제는 DB만 업데이트하고 이미 발급된 JWT의 claims는 바꾸지 않습니다. 교체하지 않으면 '결제했는데 멤버십이 없음'처럼 보입니다). 그다음 `--target home` → 홈 도착, 완전한 멤버십 상태.

## 전체 시퀀스(정상 경로)

```
1.  status                          # 환경 자가진단
2.  (2단계에서 대화로 정보 확인, 비밀번호 둘 중 택1. 생성 모드: gen-password → 사용자에게 즉시 저장시킴)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → 사용자가 메일함에서 코드 확인(유일한 대화 이탈 ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → 링크 1을 사용자에게 전송
7.  (사용자가 결제 수단 선택)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <결제 페이지 파일>          # Windows. macOS는 open, Linux는 xdg-open
    # → 사용자가 Alipay/PayPal 계산대에서 결제/승인 완료(대화 이탈 ②)
9.  query(10~15초마다) paid / ACTIVE가 될 때까지
10. refresh-login                   # ACTIVE 클레임의 새 JWT로 교체
11. login-link --target home        # → 링크 2를 사용자에게 전송
12. whoami                          # subscriptionStatus: ACTIVE 확인(선택)
13. cleanup                         # 상태 파일 정리
```

## 커맨드 → 플랫폼 API 매핑

| 스크립트 커맨드 | 플랫폼 API |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register`(multipart, 아바타 직접 업로드) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…`(링크 자체, 브라우저에서 클릭될 때 작동) |
| `create-order` | `POST /api/payment/alipay/create-order`(Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create`(Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…`(Bearer, Alipay)<br>`GET /api/subscription/create`(Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login`(`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

규칙 출처: 가입 필드와 레이트 제한은 `registration-flow.md`, 플랜과 활성화 경로는
`payment-and-activation.md`(모두 플랫폼 소스 파일 명시).

## 스크립트 수준 오류 처리

| 현상 | 처리 |
|---|---|
| `Node 版本过低`(Node 버전이 낮음) | 순수 안내 모드로 폴백. 억지로 시도하지 않음 |
| 네트워크 오류 / 타임아웃 | 1회 재시도. 그래도 실패하면 사용자에게 네트워크 확인을 부탁하고 계속(상태 파일은 남아 있으므로 처음부터 `status`로 복귀) |
| register가 비즈니스 오류(사용자 이름 중복 등) | SKILL.md 5단계 표대로 처리. **인증번호 재발송 불필요**(10분 이내면 여전히 유효) |
| register가 「邮箱验证码错误或已过期」(인증번호 오류/만료) 보고 | 시간 초과 → `send-code` 다시 실행 |
| `create-order` 후 사용자가 결제 페이지를 닫음 | 그냥 `create-order` 다시 실행(이전 주문은 2시간 후 자동 종료. PayPal PENDING 구독은 1시간 후 만료) |
| `create-order --provider paypal`이 409 반환 | 미완료 PayPal 구독이 이미 있습니다. 1시간 기다려 만료시키거나 브라우저에서 이전 승인을 완료 |
| `query`가 계속 pending / PENDING | 사용자가 결제하지 않았을 가능성. 한마디 물어보세요. 실제로 결제했다면 → payment-and-activation.md 해결 표대로 |
| `refresh-login` 403 `pending_payment` | 결제/승인이 아직 입금되지 않음. 9단계로 돌아가 폴링 계속 |
| 상태 파일 유실(실수로 삭제 / 컴퓨터 교체) | `whoami`/`refresh-login` 사용 불가. 링크 1을 열어 본 적 있는 브라우저에서 구독 페이지를 바로 새로고침해 상태를 확인하게 하거나, 다시 로그인(웹 모드) |

## 폴백 모드(순수 안내)

아래 중 하나에 해당하면 즉시 v1형 순수 안내로 물러나고, 스크립트를 더 만지작거리지 않습니다:

- Node ≥ 18이 없거나 스크립트가 같은 종류의 실패를 2회 연속한 경우;
- 사용자가 '내가 직접 웹에서 할게요'라고 명시한 경우;
- 회사/기기 정책이 스크립트의 네트워크 연결을 제한하는 경우.

폴백 후: 가입 페이지 https://global.powpow.online/register 와 구독 페이지
https://global.powpow.online/subscription 을 주고, `registration-flow.md`의 규칙에 따라 동반하며 문제를 잡습니다.
어조는 그대로, 매 턴 「다음 단계」블록으로 마무리합니다.
