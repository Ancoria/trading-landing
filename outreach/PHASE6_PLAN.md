# Phase 6 — Customer Discovery Sprint
## Target: 1 Paying Customer in 7 Days

---

## Prospect Target List — 100 Prospects Across 5 Channels

### Channel 1: Reddit (40 prospects)

Priority subs to monitor and engage:

| # | Subreddit | Size | Angle |
|---|-----------|------|-------|
| 1-10 | r/algotrading | 2.5M | Bot deployment, VPS, self-hosting threads |
| 11-15 | r/quant | 300K | Infrastructure, execution, deployment |
| 16-20 | r/selfhosted | 500K | Docker, VPS, monitoring threads |
| 21-25 | r/Python | 1.4M | Trading bot dev, deployment questions |
| 26-30 | r/cryptocurrency | 8M | Bot talk, exchange API discussions |
| 31-35 | r/mltraders | 50K | ML trading infrastructure |
| 36-38 | r/daytrading | 2M | Automation pain points |
| 39-40 | r/solana | 750K | Telegram bot deployment issues |

**Search keywords to find prospects:**
- "bot keeps crashing" / "bot died overnight"
- "VPS setup" / "how to deploy" / "host my bot"
- "auto restart" / "monitoring" / "telegram alerts"
- "API key security" / "withdrawal protection"
- "docker trading bot" / "systemd bot"
- "freqtrade deploy" / "hummingbot server"
- "woke up and bot was down"
- "3am checking positions"

### Channel 2: Discord (25 prospects)

| # | Server | Focus | Entry |
|---|--------|-------|-------|
| 41-45 | Hummingbot Discord | Market making, deployment | discord.gg/hummingbot |
| 46-50 | Freqtrade Discord | Bot strategy, hosting | discord.gg/freqtrade |
| 51-55 | Jacob's Crypto Clan | Trading signals, bots | discord.gg/jcb |
| 56-60 | Cryptohub | General crypto trading | discord.gg/cryptohub |
| 61-63 | Elite Crypto Signals | Signal automation | (invite-based) |
| 64-65 | Axion Crypto-Community | Trading education | (search Disboard) |

**Engagement strategy:** Join → read #introductions and #help channels → reply to deployment/infra questions → naturally mention your stack

### Channel 3: Telegram (20 prospects)

| # | Group Type | Angle |
|---|-----------|-------|
| 66-70 | Telegram Bot User Groups | Trojan, Maestro, Banana Gun bot users who need reliability |
| 71-75 | Crypto Trading Signal Groups | Signal automation + bot hosting |
| 76-80 | Freqtrade/Hummingbot TG Groups | Open source bot deployment help |
| 81-85 | Quant/Algo Trading Chats | Infrastructure discussions |

**Search on Telegram:** "crypto trading bot", "freqtrade", "量化交易", "trading signals", "自动交易"

### Channel 4: GitHub (10 prospects)

| # | Target | Approach |
|---|--------|----------|
| 86-90 | Freqtrade Issues/Discussions | Search "deploy", "VPS", "docker", "monitoring" |
| 91-93 | Hummingbot Discussions | Deployment and hosting questions |
| 94-95 | Jesse.trade, OctoBot, Krypto-Trading-Bot | Users asking infrastructure questions |

### Channel 5: Forums / Other (5 prospects)

| # | Platform | Angle |
|---|----------|-------|
| 96-98 | Stack Overflow | "trading bot deployment" questions |
| 99-100 | TradingView scripts | Pine Script users wanting automation |

---

## Outreach Templates — By Prospect Pain Point

### Template A: "Bot Keeps Crashing" (VPS Pain)

```
Hey — saw your [post/comment] about [bot crashing/dying overnight]. 

I built a production deployment stack that handles this: auto-restart via systemd, Telegram alerts on crash, heartbeat monitoring. It's what I run my own bots on and deploy for other traders.

Here's the setup: https://ancoria.github.io/trading-landing/

If you're still dealing with VPS headaches, happy to walk you through the architecture. No pitch — just infrastructure nerd talk.
```

### Template B: "3am Checking Positions" (Monitoring Pain)

```
Noticed you're [running a bot/checking positions manually]. I used to wake up at 3am until I built this:

https://ancoria.github.io/trading-landing/

Auto-recovery, Grafana dashboard, Telegram alerts — the stack I deploy for traders now. If you want the architecture breakdown, DM me. Not selling, just sharing what worked.
```

### Template C: "API Key Security" (Security Fear)

```
Saw your [thread/comment] on API key security. Here's how I handle it for traders:

- Trading-only keys (zero withdrawal permissions)
- Screen-share onboarding (you create the keys)
- Everything runs on YOUR server

This is the stack: https://ancoria.github.io/trading-landing/

DM me if you want the exact exchange permission config — just the setup.
```

### Template D: "How Do I Deploy This?" (Deployment Help)

```
Saw you asking about deployment. I've standardized this into a repeatable stack:

- Docker Compose (one command)
- Systemd auto-restart
- Grafana monitoring
- Telegram alerts

Here's what I deploy for traders: https://ancoria.github.io/trading-landing/

Happy to share the Docker config if it helps. Just DM.
```

### Template E: "Self-Hosted vs Cloud" (Infrastructure Decision)

```
Re: self-hosting vs cloud for trading bots — I went self-hosted with a standard stack. Cheaper, full control, and once it's set up properly you never touch it.

This is the exact setup I run and deploy: https://ancoria.github.io/trading-landing/

Key difference from a plain VPS: systemd watchdog, heartbeat monitoring, auto-recovery. The bot doesn't just run — it stays running.
```

---

## Daily Outreach Cadence (7-Day Sprint)

| Day | Target | Focus |
|-----|--------|-------|
| Day 1 | 20 DMs | Reddit (search + reply to recent threads) |
| Day 2 | 15 DMs | Reddit + join Discord servers |
| Day 3 | 15 DMs | Discord engagement + Telegram groups |
| Day 4 | 15 DMs | GitHub issues + Stack Overflow |
| Day 5 | 15 DMs | Follow-ups to anyone who replied |
| Day 6 | 10 DMs | New threads + second follow-up |
| Day 7 | 10 DMs | Final push + close any warm leads |

**Rules:**
- Never copy-paste blindly. Always reference their specific post/comment.
- No "hey sir" or "dear trader." Write like a peer.
- Link the page only when relevant. Don't spam.
- If someone replies, prioritize response over new outreach.
- Track EVERY message in the CSV.

---

## Funnel Metrics to Track

```
DM Sent ──→ Reply ──→ Call Booked ──→ Closed

Target:
100 ──→ 10 (10%) ──→ 3 (30%) ──→ 1 (33%)

Daily:
[Date] Sent: X | Replies: Y (Z%) | Calls: C | Closed: D | Revenue: $R
```

---

## Daily Report Template

```
### Day [N] Report — [Date]

**Activity**
- DMs sent today: [N]
- Total DMs sent: [N]
- Platforms: Reddit [N], Discord [N], Telegram [N], GitHub [N], Other [N]

**Funnel**
- Replies received: [N] ([X]% reply rate)
- Calls booked: [N]
- Calls completed: [N]
- Closed: [N]
- Revenue: $[N]

**Top Performing Channels**
[channel]: [N] replies from [N] DMs ([X]%)

**What's Working**
- [Template/angle that got replies]
- [Community that's most engaged]

**What's Not Working**
- [Template/angle with zero replies]
- [Community that's dead]

**Lessons Learned**
- [1-2 key insights from today's interactions]

**Next Action**
- [Specific thing to do tomorrow]
```
