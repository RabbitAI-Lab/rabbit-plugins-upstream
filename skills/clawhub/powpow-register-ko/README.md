# powpow-register

PowPow(버블) 가입 도우미(OpenClaw 버전): 새 사용자를 「버블가 뭔지 모름」에서 「계정 활성화, 정상 사용 가능」까지 데려갑니다 — 제품 소개(화면 스크린샷 포함), 단계별 가입 안내, 오류 해결, 구독 활성화 설명.

순수 안내형 스킬: 스크립트 없음, 의존성 없음. 모든 가입 작업은 사용자가 브라우저/앱에서 직접 합니다.

## 설치

```
openclaw skills install @durenzidu/powpow-register
```

## 기능

1. **제품 소개**: 약 120자 오프닝 + GitHub 공개 저장소에 호스팅된 화면 스크린샷 링크(지도 페이지, 게시글 상세 페이지 등 6장, 상황에 따라 1~3장 선택 발송).
2. **가입 안내**: 필드 규칙(사용자 이름/비밀번호/이메일 인증번호/휴대폰 번호/아바타), 서드파티 로그인(Google/Watcha/화웨이), 레이트 제한 파라미터 — 전부 플랫폼 소스 코드 출처가 명시되어 있습니다.
3. **오류 해결**: 인증번호 미수신, 사용자 이름/이메일 사용 중, 403 미활성화, 계정 잠금 등 13가지 흔한 문제.
4. **구독 활성화**: PayPal(웹) / WeChat 스캔(수동 확인) / Huawei IAP(HarmonyOS) 세 채널의 설명과 해결법. 기존 결제 경로를 그대로 재사용할 수 있고, 스킬은 길 안내만 담당합니다.

## 파일 구조

```
powpow-register/
├── SKILL.md                            # 메인 가이드(트리거 조건, 플로우, 어조 규칙)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # 필드 규칙, 레이트 제한, 오류 해결 표(출처 포함)
    ├── payment-and-activation.md       # 구독 활성화, 결제 채널, 재사용 결론
    └── screenshots.md                  # 호스팅 스크린샷 목록 + 상황 빠른 참조
```

## 보안

- 키를 전혀 포함하지 않으며, 스크립트가 없고 사용자 자격 증명에 접근하지 않습니다.
- 사용자의 비밀번호·인증번호·결제 정보를 **절대 요구하지 않습니다**. 가입과 결제는 전적으로 플랫폼 페이지에서 완료됩니다.

## 라이선스

MIT-0(ClawHub 통일 라이선스).

## 링크

- 공식 사이트: https://global.powpow.online
- 가입: https://global.powpow.online/register
- 버블 알아보기(영상): https://www.bilibili.com/video/BV1Wu826UEVz/