#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon, Wedge

PAPER, BLUE, AMBER, INK, MIST = "#FFFFFF", "#5B8DBE", "#D79D55", "#2B3440", "#A9C1D9"
GREEN, RED = "#7BA05B", "#C25B4E"
S = 512
D = "/tmp/ch_icons"
os.makedirs(D, exist_ok=True)

def canvas():
    fig = plt.figure(figsize=(S/100, S/100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 512); ax.set_ylim(0, 512)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), S, S, facecolor=PAPER, edgecolor="none"))
    return fig, ax

def hatch_lines(ax, x0, y0, x1, y1, n, color, lw=5, alpha=0.85):
    for i in range(n):
        xa = x0 + i * ((x1 - x0) / n)
        ax.plot([xa, xa + (y1 - y0)], [y0, y1], color=color, lw=lw,
                alpha=alpha, solid_capstyle="butt", zorder=2)

def save(fig, name):
    fig.savefig(os.path.join(D, name), dpi=100)
    plt.close(fig)
    print("saved", name)

# ---------- A ----------
fig, ax = canvas()
rows = [(392, BLUE), (330, AMBER), (268, RED)]
for y, c in rows:
    ax.add_patch(Circle((96, y), 13, facecolor=c, edgecolor=INK, lw=3.5, zorder=3))
    ax.add_patch(FancyBboxPatch((128, y - 11), 150, 22, boxstyle="round,pad=0.02",
                                facecolor=c, edgecolor=INK, lw=3.5, zorder=3, alpha=0.9))
lx, ly, lr = 300, 218, 118
ax.add_patch(Circle((lx, ly), lr, facecolor=PAPER, edgecolor=INK, lw=10, zorder=5))
ax.add_patch(Circle((lx, ly), lr - 16, facecolor=AMBER, edgecolor="none", zorder=6))
ax.plot([lx - 52, lx - 10, lx + 62], [ly + 2, ly - 46, ly + 50],
        color=INK, lw=22, solid_capstyle="round", solid_joinstyle="round", zorder=7)
hx, hy = lx + lr * 0.72, ly - lr * 0.72
ax.add_patch(Polygon([(hx - 16, hy + 26), (hx + 30, hy - 20), (hx + 74, hy - 64), (hx + 28, hy - 18)],
                     closed=True, facecolor=BLUE, edgecolor=INK, lw=8, zorder=4))
ax.plot([hx - 4, hx + 60], [hy + 14, hy - 50], color=INK, lw=3.5, alpha=0.75, zorder=5)
ax.plot([hx + 12, hx + 72], [hy + 26, hy - 38], color=INK, lw=3.5, alpha=0.75, zorder=5)
hatch_lines(ax, 30, 468, 130, 500, 4, BLUE, lw=5, alpha=0.6)
save(fig, "icon_A_check.png")

# ---------- B ----------
fig, ax = canvas()
cx, cy, R = 256, 268, 150
colors5 = [GREEN, AMBER, MIST, RED, "#D8DEE6"]
segs = [(210, 142), (142, 74), (74, 6), (6, -62), (-62, -134)]
for (a0, a1), c in zip(segs, colors5):
    ax.add_patch(Wedge((cx, cy), R, a1, a0, width=34, facecolor=c, edgecolor=INK, lw=5, zorder=4))
ax.add_patch(Circle((cx, cy), R - 44, facecolor=PAPER, edgecolor=INK, lw=8, zorder=5))
ax.plot([cx - 62, cx - 12, cx + 74], [cy + 2, cy - 52, cy + 58],
        color=INK, lw=24, solid_capstyle="round", solid_joinstyle="round", zorder=6)
hx, hy = cx + R * 0.68, cy - R * 0.68
ax.add_patch(Polygon([(hx - 18, hy + 30), (hx + 34, hy - 22), (hx + 84, hy - 72), (hx + 32, hy - 20)],
             closed=True, facecolor=AMBER, edgecolor=INK, lw=8, zorder=4))
ax.plot([hx, hx + 66], [hy + 18, hy - 48], color=INK, lw=3.5, alpha=0.7, zorder=5)
for y, c in [(452, BLUE), (404, AMBER)]:
    ax.add_patch(Circle((70, y), 12, facecolor=c, edgecolor=INK, lw=3.5, zorder=3))
    ax.add_patch(FancyBboxPatch((100, y - 10), 130, 20, boxstyle="round,pad=0.02",
                                facecolor=c, edgecolor=INK, lw=3.5, zorder=3, alpha=0.9))
save(fig, "icon_B_fivestate.png")

# ---------- C ----------
fig, ax = canvas()
ax.add_patch(Polygon([(96, 452), (300, 452), (368, 384), (368, 60), (96, 60)],
             closed=True, facecolor=PAPER, edgecolor=INK, lw=9, zorder=3))
ax.add_patch(Polygon([(300, 452), (300, 384), (368, 384)], closed=True,
             facecolor="#E8DFC8", edgecolor=INK, lw=6, zorder=4))
for y, c, w in [(376, GREEN, 200), (316, AMBER, 170), (256, RED, 210), (196, BLUE, 150)]:
    ax.add_patch(FancyBboxPatch((136, y - 12), w, 24, boxstyle="round,pad=0.02",
                                facecolor=c, edgecolor=INK, lw=3.5, zorder=4, alpha=0.95))
lx, ly, lr = 296, 190, 108
ax.add_patch(Circle((lx, ly), lr + 10, facecolor=PAPER, edgecolor=INK, lw=6, zorder=5))
ax.add_patch(Circle((lx, ly), lr, facecolor=BLUE, edgecolor=INK, lw=10, zorder=6))
ax.add_patch(Circle((lx, ly), lr - 18, facecolor=PAPER, edgecolor="none", zorder=7))
ax.plot([lx - 48, lx - 8, lx + 58], [ly + 2, ly - 44, ly + 46],
        color=INK, lw=20, solid_capstyle="round", solid_joinstyle="round", zorder=8)
ax.add_patch(Polygon([(lx + lr*0.70, ly - lr*0.70 + 24), (lx + lr*0.70 + 44, ly - lr*0.70 - 20),
                      (lx + lr*0.70 + 88, ly - lr*0.70 - 64), (lx + lr*0.70 + 44, ly - lr*0.70 - 20)],
                     closed=True, facecolor=AMBER, edgecolor=INK, lw=8, zorder=5))
hatch_lines(ax, 400, 30, 500, 80, 4, AMBER, lw=6, alpha=0.8)
save(fig, "icon_C_document.png")

# ---------- D ----------
fig, ax = canvas()
lx, ly, lr = 256, 262, 168
ax.add_patch(Circle((lx, ly), lr, facecolor=BLUE, edgecolor=INK, lw=12, zorder=4))
ax.add_patch(Circle((lx, ly), lr - 24, facecolor=PAPER, edgecolor=INK, lw=6, zorder=5))
ax.plot([lx - 78, lx - 16, lx + 96], [ly + 4, ly - 68, ly + 76],
        color=AMBER, lw=34, solid_capstyle="round", solid_joinstyle="round", zorder=6)
ax.plot([lx - 78, lx - 16, lx + 96], [ly + 4, ly - 68, ly + 76],
        color=INK, lw=10, solid_capstyle="round", solid_joinstyle="round", zorder=7)
ax.add_patch(Polygon([(lx + lr*0.66, ly - lr*0.66 + 30), (lx + lr*0.66 + 52, ly - lr*0.66 - 22),
                      (lx + lr*0.66 + 108, ly - lr*0.66 - 78), (lx + lr*0.66 + 52, ly - lr*0.66 - 22)],
                     closed=True, facecolor=AMBER, edgecolor=INK, lw=9, zorder=4))
hatch_lines(ax, lx + lr*0.66 + 26, ly - lr*0.66 - 60, lx + lr*0.66 + 96, ly - lr*0.66 - 20, 3, INK, lw=3.5, alpha=0.6)
save(fig, "icon_D_minimal.png")
print("ALL DONE")
