# 구독 활성화와 결제 — powpow-register

## 결론(먼저 답)

**기존 결제 수단을 그대로 재사용할 수 있어서, 등록 도우미 스킬은 결제 개발이 전혀 필요 없습니다.**

이유:

1. 등록 API(`src/app/api/auth/register/route.ts`)는 pending 계정 생성 시 이미 JWT cookie + pendingUserToken HttpOnly cookie를 발급합니다. 사용자는 `/subscription`에 도착한 시점에 이미 로그인 상태이며, 세 결제 채널 모두 이 구독 페이지에 붙어 있고 같은 pending 계정을 활성화합니다.
2. 로그인 API는 pending 계정에 403 + `redirectTo: '/subscription'`을 반환하고, 마찬가지로 cookie를 설정합니다. 사용자가 언제든 추가 결제하면 같은 페이지로 안내됩니다.
3. 따라서 등록 안내형 스킬의 책임 범위는 「사용자를 /subscription으로 안내하는 것」뿐입니다. 새 결제 API, 새 주문 모델, 백엔드 변경이 전혀 필요 없습니다.

동시에 주의: 결제 과정(PayPal JS SDK 버튼, WeChat 스캔 수동 확인, 화웨이 네이티브 IAP)은 **본질상 커맨드라인/채팅 스킬이 대리 결제할 수 없고, 해서도 안 됩니다**. 스크립트로 결제 API를 호출해 사용자를 대신해 결제하려 하거나, 사용자의 결제 정보를 요구하지 마세요.

## 구독 페이지의 세 채널

구독 페이지 `src/app/(public)/subscription/page.tsx`는 실행 환경에 따라 자동으로 채널을 보여줍니다:

| 채널 | 환경 | 메커니즘 | 활성화 방식 |
|---|---|---|---|
| PayPal 구독 | 웹(HarmonyOS 아님) | `/api/subscription/create`로 PayPal 구독 생성 → PayPal 승인으로 이동. 월 자동 갱신, 언제든 해지 가능(`/api/subscription/manage`) | PayPal Webhook(`BILLING.SUBSCRIPTION.*`)이 자동으로 `accountStatus`를 active로 설정 |
| WeChat 스캔 구독 | 웹(HarmonyOS 아님) | 페이지 하단 「WeChat 스캔 구독」 블록: QR 스캔 송금, **수동 확인 후 개통**(`WechatQrPaymentSection`) | 수동 확인. 입금 지연 가능. 결제 직후 실패로 단정하지 말 것 |
| 화웨이 인앱 결제(IAP) | HarmonyOS 앱 내 | HarmonyOS WebView에서 PayPal/WeChat 결제를 쓸 수 없어, 페이지가 네이티브 `NativeBridge.purchaseSubscription()`을 사용 | `/api/subscription/activate-huawei`가 화웨이 주문을 검증하고 활성화 |

플랜과 가격은 `/api/subscription/plans`에서 동적으로 읽어옵니다(PayPal 플랜). 페이지 고정 문구: Auto-renews. Cancel anytime.

## 상태와 이동

- 결제 성공 → `/subscription/success`(PayPal 콜백에 `subscriptionId` 포함) → 계정 active → `next` 파라미터가 지정한 원래 페이지로 자동 이동(없으면 홈).
- 이미 구독한 사용자가 구독 페이지를 다시 방문 → "You're All Set!" 표시 후 3초 뒤 자동으로 홈 복귀.
- 결제 실패/취소 → `/subscription/cancel`, 다시 시작 가능.

## 문제 해결

| 현상 | 처리 |
|---|---|
| 결제했는데 아직 403 | PayPal: Webhook이 가끔 지연됨. 재로그인으로 상태 갱신(로그인 시 DB 최신 상태 재확인). WeChat: 수동 확인 미완료, 잠시 대기. 화웨이: 앱 안에서 결제 성공 페이지가 떴는지 확인 |
| 구독 페이지에 "No subscription plans available" 표시 | `/api/subscription/plans`에 사용 가능한 PayPal 플랜 없음 — 플랫폼 측 설정 문제. 사용자에게 나중에 다시 시도하도록 안내 |
| WeChat으로 결제했는데 개통 안 됨 | 수동 확인은 비동기. 몇 시간 내에 개통되지 않으면 플랫폼 지원에 문의(dongtao@outlook.com) |

## 참고: Alipay

코드에 Alipay 웹 결제 한 벌이 있습니다(`src/lib/alipay.ts`, `/api/payment/create-order`, 일반회원 ¥9.90 / 프리미엄회원 ¥99 일시불 매수 모델, 샌드박스 키 미설정 시 자동으로 모의 결제로 폴백). **하지만 구독 페이지 UI에는 연결되어 있지 않으며**, 비활성/예약 코드입니다. 나중에 구독 페이지에서 Alipay를 활성화하려면 이 기존 코드를 연결하면 됩니다 — 이 스킬과는 무관하며, 플랫폼 측 결정을 위한 참고 정보입니다.