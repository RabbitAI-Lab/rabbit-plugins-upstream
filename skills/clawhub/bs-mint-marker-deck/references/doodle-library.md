# Marker doodle library

Use these original inline scenes to explain people working together. They carry the illustration layer of this deck style: open head contours, very small oval eyes, loose black marker strokes, a few solid hands, and a small mint or peach accent. The figures are fictional; do not treat them as portraits, mascots, or brand assets.

## Placement rules

- Place the SVG inline in the page. Do not fetch an image from another folder or website.
- Keep the complete `viewBox` and scale proportionally. Never stretch the width and height independently.
- Use one large scene on an illustration-led slide. Give it a clear action: listening, planning, explaining, or greeting.
- Let a scene crop at the slide edge only when the crop feels deliberate. Keep the hand doing the action, the shared object, and at least one face visible.
- A heading may overlap a quiet part of a scene. Keep body copy in a separate column, away from eyes, hands, or the paper boundary.
- Use the default light theme for the first slide. On a mint canvas, keep the black linework and reserve off-white for a paper surface if needed.
- Do not add tiny decorative marks to fill empty space. The oversized title and the people already provide enough visual weight.

The SVG root uses `--ink` and the paper surfaces use `--paper`, both with local fallback colors. Mint, gray, and peach are explicit colors so a theme preset can remap them when the deck is generated. The outer background is transparent. No SVG requires an external font, remote asset, filter, symbol sheet, or JavaScript.

```css
.marker-scene {
  display: block;
  width: 100%;
  height: auto;
  color: var(--ink, #0b0c0b);
  overflow: visible;
}
```

Add `class="marker-scene"` to the SVG root after pasting it. If the scene is purely decorative, replace `role="img"` and the accessible label with `aria-hidden="true"`. If it explains an action, keep the accessible label or rewrite it for the deck's actual message.

## Draw new scenes in the same language

1. Start with one interaction, not a collection of unrelated props.
2. Place the head shapes at different heights and give them different tilts. Draw each open contour as its own irregular curve; do not duplicate one head across all figures.
3. Use a 14–22 unit black stroke for large figures in a roughly 1400-unit scene, with round joins and caps. Use narrower strokes for mouths and paper details.
4. Leave bodies mostly unfilled. A shoulder, an arm, and a long curved back often tell the whole pose.
5. Keep eyes tiny compared with the head. Use a short curved mouth only where it helps the conversation.
6. Draw hands as compact irregular black shapes, placed where a gesture or contact is visible. Avoid literal finger detail unless one raised finger carries the idea.
7. Add at most one shared object and one small accent color area. A paper plan is an appropriate object; an invented interface, a real logo, or a branded device is not.
8. Draw arrows or bulbs with SVG paths. Never use emoji, Unicode pictograms, or an icon font as a substitute.

## Scene selection

| Scene | Native viewBox | Suggested use |
| --- | --- | --- |
| Shared plan | 1400 by 620 | Cover or collective action slide; nearly full-width scene |
| Folded paper | 700 by 650 | Left column of a split slide; a simple collaboration story |
| Design board | 900 by 800 | Right side of a mint divider; deliberate edge cropping |
| Gathering | 1400 by 500 | Bottom half of an objectives or discussion slide |
| Greeting | 700 by 620 | Closing or invitation slide; keep the wave visible |
| Idea bulb | 180 by 240 | One small margin accent beside an idea; never repeated as wallpaper |

All scene snippets below are complete and can be placed inline on a page without dependencies. Adapt the scene's content by drawing new paths, not by tracing reference artwork.

## Shared plan

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 620" role="img" aria-label="Three neighbors arrange a large paper plan around a shared table." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="18" stroke-linecap="round" stroke-linejoin="round">
    <!-- A leaning listener with a long, open head contour. -->
    <path d="M171 247 C142 218 126 153 145 111 C164 71 204 48 246 54 C286 57 310 86 321 123 C330 154 329 197 309 229 C298 248 282 258 263 261"/>
    <path d="M154 294 C127 326 113 387 105 443 C99 487 102 526 117 554 M240 295 C264 331 272 377 292 423"/>
    <path d="M146 340 C160 392 174 438 201 464 C241 459 291 437 339 409 L464 373"/>
    <path d="M282 349 C296 380 326 397 373 393 L458 371"/>
    <!-- A planner: narrower head, a tiny smile, and a forward lean. -->
    <path d="M583 206 C565 179 558 128 571 90 C582 55 616 32 651 35 C687 37 717 67 724 105 C732 139 730 177 710 208"/>
    <path d="M585 245 C569 279 554 310 543 348 M710 245 C729 279 740 303 759 328"/>
    <path d="M580 283 C601 307 617 329 637 350 M711 288 C693 314 681 332 666 350"/>
    <!-- A seated maker, smiling toward the group. -->
    <path d="M1055 277 C1023 262 998 219 1002 174 C1005 131 1035 99 1077 95 C1128 90 1168 125 1179 168 C1188 203 1186 245 1161 271"/>
    <path d="M1045 308 C1019 335 1009 371 1005 423 M1158 311 C1196 337 1218 394 1221 457 C1224 493 1215 529 1200 557"/>
    <path d="M1180 367 C1161 404 1134 431 1104 432 C1064 419 1025 398 982 378"/>
    <path d="M1044 350 C1012 378 985 407 950 426"/>
  </g>
  <g fill="currentColor">
    <ellipse cx="265" cy="154" rx="7.5" ry="13" transform="rotate(9 265 154)"/><ellipse cx="288" cy="151" rx="7" ry="12" transform="rotate(9 288 151)"/>
    <ellipse cx="628" cy="127" rx="7.5" ry="13" transform="rotate(-6 628 127)"/><ellipse cx="651" cy="126" rx="7" ry="12"/>
    <ellipse cx="1045" cy="192" rx="7" ry="12" transform="rotate(-11 1045 192)"/><ellipse cx="1069" cy="190" rx="7.5" ry="13" transform="rotate(-11 1069 190)"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">
    <path d="M630 169 C641 178 655 178 667 167"/><path d="M1049 229 C1061 241 1078 238 1087 227"/>
    <path d="M233 207 C244 211 253 209 263 203"/>
  </g>
  <path d="M355 515 C533 529 806 548 1106 532 M399 542 L385 598 M1054 554 L1079 608" fill="none" stroke="#9d9d99" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- This is a loose original paper shape, not a source asset. -->
  <path d="M436 351 L942 329 L1063 507 L527 534 Z" fill="var(--paper, #f1f0ea)" stroke="currentColor" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M571 398 L783 385 L825 459 L621 470 Z M877 388 L947 393 M892 425 L969 431" fill="none" stroke="#3eaf9d" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M585 443 L719 436 M704 409 L725 454" fill="none" stroke="#9d9d99" stroke-width="7" stroke-linecap="round"/>
  <g fill="currentColor">
    <path d="M439 346 C450 338 469 347 474 359 C483 375 472 394 461 398 C449 401 430 385 428 372 C426 361 430 353 439 346 Z"/>
    <path d="M621 337 C634 327 648 333 653 344 C656 357 652 379 644 384 C632 390 611 375 610 363 C609 352 614 343 621 337 Z"/>
    <path d="M655 339 C667 329 685 334 690 347 C695 362 690 379 678 386 C663 388 649 376 648 363 C646 352 649 344 655 339 Z"/>
    <path d="M968 362 C980 351 995 356 1001 368 C1007 381 1000 398 988 403 C975 408 954 390 954 380 C954 372 960 367 968 362 Z"/>
    <path d="M931 408 C943 400 959 404 965 416 C969 428 962 444 952 449 C939 451 924 443 920 433 C917 423 923 414 931 408 Z"/>
  </g>
</svg>
```

## Folded paper

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 650" role="img" aria-label="Two collaborators share and discuss a folded paper sketch." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="17" stroke-linecap="round" stroke-linejoin="round">
    <path d="M111 259 C80 231 73 178 91 133 C108 94 144 73 183 82 C225 91 252 127 252 169 C253 210 242 238 222 258"/>
    <path d="M111 296 C82 333 74 401 77 459 C77 512 92 563 105 593 M223 300 C242 328 249 363 250 389"/>
    <path d="M125 355 C142 395 150 445 174 464 L288 427"/>
    <path d="M233 340 C263 365 290 381 327 381"/>
    <path d="M506 286 C477 272 455 231 459 189 C462 143 485 111 525 107 C569 102 601 130 613 170 C625 210 616 257 596 277"/>
    <path d="M507 314 C477 351 464 386 462 426 M593 314 C626 353 641 413 636 472 C631 512 623 549 604 588"/>
    <path d="M484 363 C462 397 447 414 411 424 M607 368 C581 412 559 442 531 448 L444 430"/>
  </g>
  <g fill="currentColor">
    <ellipse cx="193" cy="169" rx="7" ry="12" transform="rotate(9 193 169)"/><ellipse cx="215" cy="167" rx="7" ry="11" transform="rotate(9 215 167)"/>
    <ellipse cx="485" cy="207" rx="7" ry="12" transform="rotate(-10 485 207)"/><ellipse cx="508" cy="203" rx="7" ry="12" transform="rotate(-10 508 203)"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round">
    <path d="M188 214 C201 223 212 219 220 210"/><path d="M488 248 C500 251 511 247 521 240"/>
  </g>
  <path d="M302 326 L406 303 L465 447 L346 469 L275 405 Z" fill="var(--paper, #f1f0ea)" stroke="currentColor" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M302 326 L346 469 M323 368 L390 353 M337 399 L408 386" fill="none" stroke="#3eaf9d" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="currentColor">
    <path d="M311 364 C322 355 338 359 343 371 C350 385 341 399 328 401 C315 401 303 391 302 381 C301 375 305 368 311 364 Z"/>
    <path d="M278 409 C290 401 304 406 308 418 C313 431 307 445 294 449 C281 452 269 442 268 431 C267 422 270 414 278 409 Z"/>
    <path d="M424 411 C436 402 450 407 455 419 C459 431 454 446 442 449 C429 450 416 440 415 430 C414 422 417 415 424 411 Z"/>
  </g>
  <path d="M121 606 C246 613 446 614 578 605" fill="none" stroke="#9d9d99" stroke-width="8" stroke-linecap="round"/>
</svg>
```

## Design board

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 800" role="img" aria-label="Two makers gesture toward a large shared design board." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="21" stroke-linecap="round" stroke-linejoin="round">
    <path d="M224 292 C188 274 169 222 183 170 C195 121 236 85 282 88 C328 91 367 130 368 181 C370 224 356 263 339 278"/>
    <path d="M224 326 C192 370 176 435 174 494 M339 323 C360 343 378 371 389 411"/>
    <path d="M191 394 C174 372 158 329 152 274 C142 241 116 224 88 206 L25 177"/>
    <path d="M353 373 C384 406 404 425 443 425"/>
    <path d="M751 307 C708 287 688 246 695 194 C701 144 733 108 781 113 C832 117 866 156 868 204 C871 247 856 279 840 295"/>
    <path d="M741 346 C712 390 704 438 709 494 M846 339 C875 372 892 433 889 485 C885 542 867 595 858 643"/>
    <path d="M865 401 C841 447 814 478 778 481 L707 463"/>
    <path d="M722 402 C699 423 685 446 677 477"/>
  </g>
  <g fill="currentColor">
    <ellipse cx="277" cy="187" rx="8" ry="14" transform="rotate(7 277 187)"/><ellipse cx="301" cy="185" rx="8" ry="13"/>
    <ellipse cx="727" cy="219" rx="8" ry="13" transform="rotate(-7 727 219)"/><ellipse cx="751" cy="216" rx="7.5" ry="13"/>
    <path d="M17 159 C32 148 52 156 61 170 L79 173 C89 177 97 193 92 204 C81 221 66 226 50 218 L21 192 C8 181 8 168 17 159 Z"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round">
    <path d="M273 238 C281 227 297 225 309 229"/><path d="M730 258 C742 269 758 267 771 254"/>
  </g>
  <path d="M390 370 L725 354 L788 638 L434 684 L359 581 Z" fill="var(--paper, #f1f0ea)" stroke="currentColor" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M435 416 L538 409 L559 480 L451 490 Z M586 407 L678 399 L698 472 L604 483 Z" fill="none" stroke="#3eaf9d" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M464 553 C493 521 526 516 555 530 C584 543 607 564 644 550 M645 550 L682 526 M645 550 L686 575 M478 619 L673 600" fill="none" stroke="#9d9d99" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="currentColor">
    <path d="M424 405 C439 394 457 399 464 414 C471 430 462 447 448 451 C432 453 416 441 415 427 C414 418 418 411 424 405 Z"/>
    <path d="M681 457 C697 446 716 451 722 466 C729 482 721 499 705 503 C689 503 674 491 673 477 C672 469 676 462 681 457 Z"/>
    <path d="M656 474 C673 461 687 466 694 482 C700 497 692 515 677 517 C664 519 650 507 647 494 C645 485 650 478 656 474 Z"/>
  </g>
  <path d="M429 701 L412 770 M746 668 L768 756" fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round"/>
</svg>
```

## Gathering

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 500" role="img" aria-label="Four neighbors share ideas in a relaxed seated conversation." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="18" stroke-linecap="round" stroke-linejoin="round">
    <!-- Wide head and outward leaning listening posture. -->
    <path d="M120 236 C91 217 81 174 95 133 C109 92 143 64 183 67 C227 70 257 107 255 151 C254 190 239 218 221 232"/>
    <path d="M124 265 C95 289 87 334 94 376 C101 408 133 422 165 424 M223 264 C251 295 267 331 275 370"/>
    <path d="M104 305 L42 396 M249 309 C277 340 300 356 338 347"/>
    <!-- Tall maker with an open head and raised hand. -->
    <path d="M444 202 C418 177 419 136 436 106 C455 76 489 65 520 73 C555 81 579 112 578 146 C578 174 566 201 550 213"/>
    <path d="M444 243 C417 271 402 314 402 364 C402 402 434 428 477 431 C520 435 558 426 581 402 C588 374 584 340 572 310 C563 283 551 259 541 246"/>
    <path d="M544 261 C590 247 615 224 620 189 L627 80 M423 285 C393 311 364 326 344 340"/>
    <!-- Rounded maker, forward lean, both hands explaining. -->
    <path d="M766 218 C740 200 730 163 738 129 C746 90 777 66 814 69 C851 74 877 102 882 134 C889 169 880 200 865 216"/>
    <path d="M764 249 C739 276 723 312 720 357 C716 395 735 424 776 432 C812 439 850 433 878 415 C888 375 885 337 875 305 C868 278 861 262 851 249"/>
    <path d="M733 291 C693 326 669 339 647 337 M865 287 C905 315 938 332 969 330"/>
    <!-- Narrow head and crossed-leg posture. -->
    <path d="M1131 236 C1109 214 1103 174 1113 137 C1123 102 1151 82 1182 84 C1217 86 1244 116 1247 150 C1252 187 1242 218 1227 234"/>
    <path d="M1137 264 C1108 292 1097 329 1099 373 M1225 267 C1254 304 1269 347 1266 393 C1258 419 1239 435 1211 437"/>
    <path d="M1121 308 C1097 334 1069 347 1030 340 M1237 307 C1229 350 1215 373 1184 380 L1127 376"/>
    <path d="M1188 408 C1155 388 1129 371 1104 391 L1047 454 M1102 401 L1062 378 L1009 447"/>
  </g>
  <g fill="currentColor">
    <ellipse cx="202" cy="151" rx="7" ry="12"/><ellipse cx="224" cy="149" rx="7" ry="12"/>
    <ellipse cx="493" cy="137" rx="7" ry="12" transform="rotate(6 493 137)"/><ellipse cx="516" cy="137" rx="7" ry="12"/>
    <ellipse cx="775" cy="150" rx="7" ry="12" transform="rotate(-8 775 150)"/><ellipse cx="799" cy="148" rx="7" ry="12" transform="rotate(-8 799 148)"/>
    <ellipse cx="1139" cy="166" rx="7" ry="12"/><ellipse cx="1161" cy="164" rx="7" ry="12"/>
    <path d="M331 332 C343 323 357 325 364 337 C370 349 365 363 354 365 C340 370 326 358 323 347 C322 341 326 336 331 332 Z"/>
    <path d="M615 66 C619 48 629 39 638 42 C647 46 645 65 644 76 L657 70 C669 70 677 81 673 91 C672 104 659 115 645 122 C633 120 622 112 617 101 C611 88 612 78 615 66 Z"/>
    <path d="M629 322 C641 314 656 318 661 329 C666 342 660 356 648 359 C636 361 622 350 621 339 C620 332 624 325 629 322 Z"/>
    <path d="M952 315 C964 307 980 312 985 325 C990 337 982 351 971 354 C958 355 945 345 944 334 C944 326 947 320 952 315 Z"/>
    <path d="M1010 327 C1022 317 1038 321 1043 334 C1049 347 1042 360 1030 364 C1017 366 1003 355 1002 344 C1001 337 1005 331 1010 327 Z"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round">
    <path d="M193 191 C205 198 219 195 228 186"/><path d="M493 180 C504 185 514 181 522 174"/><path d="M777 189 C788 198 803 198 814 187"/><path d="M1139 210 C1151 201 1164 201 1175 204"/>
  </g>
  <path d="M58 471 C341 463 572 479 789 476 C983 473 1199 467 1314 475" fill="none" stroke="#9d9d99" stroke-width="7" stroke-linecap="round"/>
</svg>
```

## Greeting

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 620" role="img" aria-label="Two makers greet one another, one carrying a bright paper folder." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="18" stroke-linecap="round" stroke-linejoin="round">
    <path d="M115 238 C90 214 82 171 92 132 C103 93 136 65 175 72 C213 77 239 111 241 149 C243 186 232 217 214 236"/>
    <path d="M119 270 C89 304 76 359 82 412 C83 456 90 494 103 528 M214 272 C241 305 252 344 252 383"/>
    <path d="M102 322 C119 365 136 390 163 397 L215 387 M231 315 C258 339 280 353 307 356"/>
    <path d="M472 253 C445 230 435 187 448 145 C461 105 490 82 527 88 C570 94 595 129 594 169 C594 204 582 236 568 248"/>
    <path d="M472 281 C444 314 433 362 432 406 C431 450 443 491 458 530 M568 284 C593 317 608 356 611 399 C613 446 602 494 588 532"/>
    <path d="M453 326 C418 305 407 276 409 242 L415 173 M588 330 C566 370 544 391 517 391"/>
  </g>
  <g fill="currentColor">
    <ellipse cx="182" cy="158" rx="7" ry="12" transform="rotate(8 182 158)"/><ellipse cx="204" cy="156" rx="7" ry="12"/>
    <ellipse cx="470" cy="177" rx="7" ry="12" transform="rotate(-8 470 177)"/><ellipse cx="493" cy="175" rx="7" ry="12"/>
    <path d="M407 156 C405 136 411 122 419 124 C427 127 426 143 428 155 C431 140 437 135 442 141 C447 149 442 164 438 173 C449 173 458 181 455 192 C451 207 439 218 426 216 C412 214 402 204 401 191 C400 178 402 164 407 156 Z"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round">
    <path d="M177 201 C189 211 204 207 214 194"/><path d="M470 216 C482 225 497 221 507 208"/>
  </g>
  <path d="M192 341 L302 334 L322 477 L210 487 Z" fill="var(--paper, #f1f0ea)" stroke="#efbc9d" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M226 368 L269 363" fill="none" stroke="#9d9d99" stroke-width="7" stroke-linecap="round"/>
  <g fill="currentColor">
    <path d="M203 372 C214 363 229 368 234 380 C239 392 231 405 220 408 C207 410 195 400 194 389 C193 382 197 375 203 372 Z"/>
    <path d="M294 342 C306 334 320 337 326 349 C333 362 326 376 314 380 C301 382 288 371 286 361 C285 353 289 346 294 342 Z"/>
    <path d="M501 376 C513 368 528 372 533 384 C538 396 531 409 519 413 C506 415 493 404 492 394 C491 386 495 380 501 376 Z"/>
  </g>
  <path d="M96 550 C252 560 431 554 603 550" fill="none" stroke="#9d9d99" stroke-width="7" stroke-linecap="round"/>
</svg>
```

## Idea bulb

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 240" role="img" aria-label="A hand-drawn light bulb symbol." style="color:var(--ink, #0b0c0b)">
<g fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">
    <path d="M69 169 C66 145 50 139 38 115 C19 78 42 33 76 25 C111 17 145 43 147 77 C149 111 122 129 112 151 L108 170"/>
    <path d="M69 178 L108 180 M70 193 L105 196 M75 210 C80 222 99 224 103 211 M82 165 L76 93 C91 118 109 107 115 90 M87 164 L104 94"/>
  </g>
</svg>
```

