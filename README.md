# AI Department (working title)

An AI department for small businesses. A diagnostic learns the business and keeps a live top 5 of AI tools worth adopting. We set those tools up for them, keep them running every month, and offer a private local AI server to clients whose data can't leave the office.

Stage: **idea / validation**. Nothing is built yet. Read [docs/origin-conversation.md](docs/origin-conversation.md) to see how the idea started.

## The problem

- **FOMO.** Owners feel their competitors are pulling ahead with AI.
- **Overwhelm.** There are too many tools and too much news, and nobody running a business can follow it all.
- **Setup.** Even when owners know what to use, they can't connect it to their email, CRM and data, or train their staff on it.
- **Privacy.** Some businesses legally can't put client data into cloud AI: lawyers, accountants, doctors, financial advisors.

## The original idea

Two parts, combined into one business:

1. **SaaS diagnostic.** Small business owners subscribe. Onboarding asks questions until the model knows the whole business: marketing, revenue, sales process. It then keeps a live, constantly updated **top 5 AI tools to implement**. Clicking a tool walks them through setting it up.
2. **Local AI box.** A preconfigured Mac Mini (or similar machine) running local AI models, a local CRM and an agent that helps build tools when needed, all on the client's own hardware. The client buys the box, pays a monthly software fee and gets a guided onboarding.

## Recommended shape (first analysis)

1. **Free diagnostic.** It takes about 15 minutes, pulls from the business's connected tools (website, Gmail, Stripe, CRM), asks only what's missing, and returns a personal top 5 with estimated hours saved per week. It's the lead magnet, not the subscription.
2. **Paid setup.** A fixed price per tool installed.
3. **Monthly upkeep.** We keep what we installed running, add new picks as they appear and train staff. A monthly fee for staying current only holds up when it's attached to tools they actually use.
4. **Local box as a premium tier**, only for clients whose confidentiality is a legal duty.

**Pick one industry.** Within one industry the top 5 is about 80% the same for every business, so each setup package is built once and sold many times. Across all small businesses, every setup is custom and it turns into hourly consulting.

## Known risks

- **A list alone loses subscribers.** Once the top tools are installed, the list stops changing much. The value has to be implementation plus upkeep.
- **ChatGPT and Claude already make recommendations.** An owner can ask them "which AI tools should I use?" The edge has to be the setup and the industry focus, not the advice.
- **The cloud diagnostic and the privacy box contradict each other.** A cloud SaaS that learns everything about a business collects exactly the data the box promises to protect. Decide what stays local and what doesn't.
- **Local models are weaker than Claude or GPT**, especially at building tools and code. The box will likely need an honest hybrid: sensitive data and search stay local, heavy reasoning goes to a cloud model with zero data retention, and the client is told.
- **The box turns us into IT support:** hardware failures, backups, updates, remote access for staff, and security. An agent with access to a client's email and CRM is a liability if it leaks.
- **Branding:** you can resell Macs with your software installed, but putting your own brand on Apple hardware runs into Apple's trademark and reseller terms. A non-Apple mini PC can be white-labeled.
- **Replacing a client's CRM is a migration project.** Plug into what they already use.

## Open questions

- [ ] Which industry first? Criteria: confidentiality is a legal duty, owners have budget, the same tools work across firms, and we can reach owners.
- [ ] Pricing: setup fee per tool, monthly fee, and hardware (does the client buy it directly?).
- [ ] What the diagnostic pulls from connected tools vs what it asks.
- [ ] Local/cloud policy for the box: what runs where, and how it's explained to clients.
- [ ] Hardware: resold Mac Mini vs own-brand mini PC.
- [ ] Legal: GDPR, data processing agreements, liability for what agents do.
- [ ] Affiliate commissions from recommended tools: extra revenue vs trust.
- [ ] Who does what between the two founders: selling, building, delivering.

## Validation plan (before building anything)

1. Pick one industry.
2. Have 10 conversations with business owners in it.
3. For 3 of them, run the diagnostic by hand with Claude, deliver their top 5, and quote the setup of #1.
4. **Go signal:** at least 3 of 10 are ready to pay for a setup.
5. Only then build the diagnostic as software.

## Website preview

`site/index.html` is the whole site in one file:
- the landing page: how it works, the local service, pricing;
- a clickable app preview: onboarding, then the Chat, Top 5, News and Local tabs.

The Top 5 is ranked in the page from the onboarding answers. The chat uses Claude when the page is opened as a Claude artifact. Anywhere else it falls back to scripted answers. The news items are sample stories. Nothing a visitor types is sent anywhere.

- **Preview locally:** run `python3 site/dev_server.py`, then open http://localhost:4173. Add `#app` to the URL to open the app.
- **Published version:** Jerome's Claude artifact, which is private until he shares it.

## Repo layout

- `README.md`: the current concept. Keep it up to date as decisions are made.
- `site/`: the landing page and app preview (see above).
- `CLAUDE.md`: context and working rules for Claude Code.
- `docs/origin-conversation.md`: the conversation the idea came from.
- `docs/decisions.md`: a log of decisions made.
- `docs/research/`: research notes, one file per topic.
