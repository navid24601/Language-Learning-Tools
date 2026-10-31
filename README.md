# Language-Learning-Tools

Five independent skills help you learn and use English in Codex. Ask for a quick answer, a deeper explanation, feedback, or practice.

| Skill | Try saying |
|---|---|
| Vocabulary | “Teach me *resilient* at B1 level.” |
| Grammar | “Explain the present perfect briefly.” |
| Writing | “Help me improve this email without changing my tone.” |
| Speaking | “Roleplay a job interview; give feedback at the end.” |
| Translator | “Translate this into English and explain the idiom.” |

Tell the skill your level, preferred explanation language and how much detail or feedback you want. You can ask naturally or invoke a skill explicitly, such as `$vocabulary` or `$grammar`. In a quiz, ask for a hint or the answer whenever you need it.

## Install in Codex

This project includes a separate local marketplace for testing. If you have its `local-marketplace` folder, register it once in a terminal:

```powershell
codex plugin marketplace add "<absolute path to local-marketplace>"
```

Restart the desktop app, open the Plugins Directory, select **Language Learning Local**, and install **language-learning-tools**. Start a new chat to use it. If already installed, refresh or reinstall after the marketplace copy is updated. Local marketplace availability depends on your host; see [OpenAI’s plugin packaging guide](https://developers.openai.com/plugins/build/plugins) for details.

The skills work independently and need no Python, server or account connection. Speaking practice in text cannot assess pronunciation; audio feedback depends on the host’s actual capabilities. The plugin does not save progress or schedule reviews.

## Development

The marketplace holds a copy of this project; update that copy before refreshing an installed plugin. Run `python tests/validate.py` to check the package structure. Python is needed for this developer check, not for using the skills. See the [evaluation guide](evals/README.md) and [roadmap](docs/roadmap.md); structural checks do not measure teaching quality or learning outcomes.
