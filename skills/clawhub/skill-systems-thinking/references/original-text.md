# Reference: Original Text — Engineering Cybernetics

Direct excerpts from Qian Xuesen (钱学森) & Song Jian (宋健), *Engineering Cybernetics*
(工程控制论). Used here under fair use for scholarship and skill development. The original
book and its mathematical foundations are the authoritative source; this skill is a faithful
interpretation, not a replacement.

---

## §1.1 稳定性的基本要求（节选）

> 对于控制工程来说，稳定性是第一个要求。一个系统即使能在某些工作点给出正确
> 的输出，但在扰动下发散、振荡或泄漏，这个系统就是**不稳定**的——无论其设计
> 多么巧妙，都是没有实用价值的。

This is the anchor for the law "Stability before everything." An LLM must verify
perturbation behavior before proposing any feature or optimization.

---

## §1.5 控制量与受控量（节选）

> 受控量 x 是必须保持正确的量；控制量 u 是我们有自由施加作用的量。线性
> 调节理论假定变量无界——但物理系统都有界。忽略边界会使"过渡过程时间与
> 步长无关"这一结论在实践中不成立。

This is the anchor for the principle "Name x before u; respect bounds." Every actuator
saturates; every loop must have an explicit bound.

---

## §3.7 反馈的基本作用（节选）

> 反馈同时提高了准确度和响应速度。开环系统没有从误差中恢复的路径；闭环
> 系统通过"作用→观测→校正"实现收敛。

This is the anchor for "Closed loop beats open loop." After every non-trivial change,
observe the actual state before declaring success.

---

## §6.3 多变量控制的解耦（节选）

> 当两个变量之间不应相互干扰时，应当使交叉项为零——隔离、单一职责、纯函数、
> 无共享可变状态。一旦对角化，每个子系统就可以作为独立的单变量系统设计，
> 从而大幅简化问题。

This is the anchor for "Decouple what hurts, coordinate what helps."

---

## §11 时滞系统（节选）

> 时滞是稳定性的敌人。在回路延迟很大时，提高增益往往不是解决滞后响应的
> 方法——它会 pushing the system toward instability。应当降低回路增益，或添加
> 阻尼，或缩短回路。

This is the anchor for "Never crank gain on a delayed loop; add damping instead."
