# Phase 6 — Customer Discovery Sprint: EXECUTION PACK
## Day 1 Starter: 20 Live Threads to Engage NOW

Target subreddits: r/algotrading, r/selfhosted, r/Hummingbot, r/mltraders, r/freqtrade

### HIGH-PRIORITY (reply to OP or top comment thread)

1. **r/algotrading — "my first live bot"**
   https://reddit.com/r/algotrading/comments/1nu713c/
   Angle: Template A — "congrats on going live. here's what i wish i knew about crash recovery"

2. **r/algotrading — "personal bot or freqtrade bot?"**
   https://reddit.com/r/algotrading/comments/1mq3nq4/
   Angle: Template D — "depends on infra. here's the stack that works for both"

3. **r/algotrading — "Freqtrade Hyperopts / Backtesting and VPS"**
   https://reddit.com/r/algotrading/comments/1kexkvt/
   Angle: Template A — "freqtrade on VPS. here's the systemd config that prevents 3am crashes"

4. **r/algotrading — "How to officially deploy strategy live?"**
   https://reddit.com/r/algotrading/comments/1jbze91/
   Angle: Template D — "docker + systemd. here's a production-ready template"

5. **r/algotrading — "What Python Trading Platform/API?"**
   https://reddit.com/r/algotrading/comments/1i4t9e6/
   Angle: Template E — "infrastructure matters more than platform. proven stack inside"

6. **r/algotrading — "Accidental 5-month hold test"** (bot running 5 months unattended)
   https://reddit.com/r/algotrading/comments/1ppzjdt/
   Angle: Template B — "how do you monitor it? here's my setup"

7. **r/algotrading — "For those running a bot, how many hours?"**
   https://reddit.com/r/algotrading/comments/1k3rt5c/
   Angle: Template A — "most hours are infra, not strategy. deploy stack cuts it to zero"

8. **r/selfhosted — "the0 - Open source algo-trading bot orchestration"**
   https://reddit.com/r/selfhosted/comments/1nl360i/
   Angle: Template E — "nice project. here's a production deployment stack"

9. **r/mltraders — "Trading Bot"** (mentions Prometheus, Docker, health checks)
   https://reddit.com/r/mltraders/comments/1mopjuh/
   Angle: Template B — "prometheus + grafana. here's my full monitoring config"

10. **r/Hummingbot — "Any active builders & traders here?"**
    https://reddit.com/r/Hummingbot/comments/1scav92/
    Angle: Template A — "running HB in prod. here's the deployment stack that keeps it alive"

### MEDIUM-PRIORITY (newer threads, active discussion)

11. **r/Hummingbot — "AttributeErrors when connecting to paper trades"**
    https://reddit.com/r/Hummingbot/comments/1msqox7/
    Angle: Template A — "deployment guide + common pitfalls"

12. **r/algotrading — "New to algo trading – where should I start?"**
    https://reddit.com/r/algotrading/comments/1ms4ljw/
    Angle: Template D — "skip the tool debate. here's the infra you'll need either way"

13. **r/Daytrading — "Anyone here successfully built a trading bot?"**
    https://reddit.com/r/Daytrading/comments/1j1m12r/
    Angle: Template B — "monitoring is the hard part. here's how"

14. **r/Trading — "I have a simple profitable strategy, what's the chances?"**
    https://reddit.com/r/Trading/comments/1jf10qt/
    Angle: Template D — "strategy is 30%. infra is 70%. deploy stack here"

15. **r/selfhosted — "Whats the point in a VPS?"**
    https://reddit.com/r/selfhosted/comments/1t2ff9c/
    Angle: Template E — "for trading bots: VPS + auto-recovery = sleep. here's the config"

### DISCOVERY (search these terms daily on Reddit)

- "bot stopped" "bot crashed" "bot died" "bot went down"
- "how to deploy" "how to host" "VPS setup" "server setup"
- "freqtrade VPS" "freqtrade server" "freqtrade docker"
- "hummingbot deploy" "hummingbot server" "hummingbot VPS"
- "trading bot monitoring" "telegram alert bot"
- "API key security" "exchange API key" "trading API key"
- "auto restart bot" "systemd bot" "docker trading"
- "woke up" "3am" "checking positions" "missed trade"

---

## Discord Entry Points (Day 2-3)

| Server | Invite | #help Channel | Strategy |
|--------|--------|---------------|----------|
| Hummingbot | https://discord.gg/hummingbot | # deployment-help | Answer Docker/VPS questions |
| Freqtrade | https://discord.gg/p7nuUNVfP7 | #installation | Help with systemd/docker setup |
| Jacob's Crypto Clan | https://discord.gg/jcb | #bot-discussion | Discuss automation reliability |
| Cryptohub | https://discord.gg/cryptohub | #trading-tools | Infrastructure pain points |

**Discord Rules:**
- Join. Wait 24h before posting. Read pinned messages first.
- Answer 3 questions before mentioning your service.
- When you do: "I run this stack for traders" NOT "buy my service"
- Your Discord bio should link to the landing page.

---

## Telegram Discovery (Day 3-4)

Search in Telegram for these group names:
- "freqtrade" / "Freqtrade 中文"
- "hummingbot" / "Hummingbot 中文"  
- "crypto trading bot" / "加密货币交易机器人"
- "量化交易" / "algo trading"
- "交易机器人部署" / "trading bot deploy"
- "Binance API" / "OKX API"

**Telegram Strategy:**
- Join 10 groups. Listen for 2 days.
- When someone asks about deployment/crashing/monitoring → offer specific technical help
- Link to the page only after providing value first
- Pin: the Chinese crypto trader community is underserved on infrastructure

---

## GitHub Discovery (Day 4-5)

Search these repos for open deployment issues:
- `github.com/freqtrade/freqtrade/issues` — search: "deploy", "docker", "VPS", "monitoring", "crash"
- `github.com/hummingbot/hummingbot/issues` — search: "server", "hosting", "deployment", "connection"
- `github.com/jesse-ai/jesse` — search: "deploy", "live", "production"
- `github.com/ccxt/ccxt` — search: "production", "deployment"

Look for issues tagged `help-wanted` or `question` where users are clearly struggling with ops.

---

## Daily Execution Checklist

### Every Morning (15 min)
- [ ] Search Reddit for new threads matching discovery keywords
- [ ] Check CSV for unreplied DMs → follow up
- [ ] Open Discord/Telegram → scan for deployment questions

### Every Evening (15 min)  
- [ ] Update tracker.csv with today's activity
- [ ] Fill daily report section below
- [ ] Note top-performing angle for tomorrow

---

## Funnel Dashboard

### Current Status
```
Day: 0 (pre-launch)
DMs Sent: 0
Replies: 0 (0%)
Calls Booked: 0
Calls Completed: 0  
Closed: 0
Revenue: $0
```

### Target
```
Day 7:
DMs Sent: 100
Replies: 10+ (10%+)
Calls Booked: 3+
Closed: 1+
Revenue: $199+
```

---

## Reply Playbook (What to Do When Someone Replies)

### Reply Type 1: Technical Question
"That's interesting — what do you use for monitoring?"
→ Answer in detail. Share a specific config snippet. Offer DM for more.

### Reply Type 2: Price Objection
"$199 for a setup? I can do it myself."
→ "Fair. The $199 is for people who value 48h turnaround over 2 weeks of debugging systemd configs. If you're comfortable with ops, the architecture is all open source on the page."

### Reply Type 3: Trust Question  
"How do I know you won't steal my API keys?"
→ "You create the keys. Trading-only permissions. Screen-share onboarding. Everything stays on your server. I'll walk you through the exchange permission config right now if you want."

### Reply Type 4: "Tell Me More"
→ "DM me. I'll share the Grafana dashboard + architecture diagram. 15 minutes, no pitch."

### Reply Type 5: Call Booked
→ Send Calendly/Telegram. Prepare: architecture diagram, Grafana screenshot, Docker compose file. Close with: "When do you want to go live?"

---

## Critical Rules

1. **Never sell in the first message.** Link to page. Offer help. Let the page sell.
2. **Personalize every DM.** Reference their specific problem. No templates pasted raw.
3. **Speed > perfection.** A 2-sentence reply in 5 minutes beats a perfect reply in 2 hours.
4. **Volume is the strategy.** 100 DMs → 10 replies → 3 calls → 1 close. It's math.
5. **Track everything.** If it's not in the CSV, it didn't happen.
6. **Don't build anything.** No new pages, no new features, no new tools. Sell what exists.
