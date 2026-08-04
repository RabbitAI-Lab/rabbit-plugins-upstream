# tokio::sync::Mutex guard lifetime — `if let` deadlock trap

## The pattern

When using `tokio::sync::Mutex` (or any non-reentrant async mutex), the
`MutexGuard` from a `lock().await` inside an `if let` scrutinee lives for the
**entire body** of the `if let` block, not just the scrutinee expression:

```rust
// 🔴 DEADLOCK — guard lives through the entire if-let body
if let Some(peer) = peer_map.lock().await.get_mut(&addr) {
    // guard produced by lock().await is still alive here
    peer.login = login.clone();
    peer.authenticated = true;
    // ... more work that doesn't re-lock — fine so far ...

    // ⚠️ IF you call something that locks the same mutex here:
    broadcast_to_room(&peer_map, &addr, ...).await?;
    //        ^^^^^^^^^     second lock().await on same Mutex
    //        The task awaits a lock it already holds — hangs forever.
}
```

This applies to both `if let` and `let ... = ` in `match` arms when the
scrutinee contains `lock().await`:

```rust
// 🔴 Also deadlocks
match peer_map.lock().await.get_mut(&addr) {
    Some(peer) => {
        broadcast_to_room(...).await?;  // deadlock
    }
    None => {}
}
```

## Why `std::sync::Mutex` makes this harder to spot

With `std::sync::Mutex`, the guard is a `LockResult<MutexGuard>` that is held
for a scope. Many `if let` patterns with `std::sync::Mutex` DON'T deadlock in
practice because the guard is dropped at the end of the expression in Rust
editions before 2024. But `tokio::sync::Mutex` has the same semantics — it's
**NOT reentrant** — so the same structural pattern causes an **async deadlock**
instead of a panic.

## The fix

Bind the result to a **local variable first** so the guard's scope ends at the
`let` statement:

```rust
// ✅ SAFE — guard is dropped after `let` statement
let removed = peer_map.lock().await.remove(&addr);
if let Some(peer) = removed {
    // guard is already released — safe to re-lock
    broadcast_to_room(&peer_map, &addr, ...).await?;
}
```

Or equivalently with a block scope:

```rust
let peer_info = {
    let mut peers = peer_map.lock().await;
    peers.get_mut(&addr).map(|p| (p.login.clone(), p.authenticated))
};
// guard dropped here
```

## Detection in adversarial review

This pattern is easy to miss in a code diff because the `if let` scrutinee is
often formatted as:

```rust
if let Some(peer) = peer_map.lock().await.get_mut(&addr) {
```

To a reviewer reading line by line, this reads as "lock, get, check". The
deadlock only manifests when a **subsequent call** in the body (possibly many
lines below) also locks the same mutex. Cross-review between two models catches
this because one model focuses on the lock acquisition and retention while the
other traces the data flow through the body.

## When it applies

- `tokio::sync::Mutex` ONLY (not `std::sync::Mutex` — though the same
  structural issue causes a runtime panic there, which is easier to spot)
- Any non-reentrant async mutex
- Any control flow where `lock().await` is inside the scrutinee expression of
  `if let`, `while let`, or `match`
