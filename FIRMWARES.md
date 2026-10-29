# FM-1 Firmware Atlas

68 firmwares for the M-VAVE FM-1. Built 2026-10-29 from `data/firmwares.json` and GitHub activity in `data/github-meta.json`.

Health: active = pushed within 14 days, quiet = 15-60 days, stale = older. The scene started July 2026, so stale means abandoned-looking here.

## Classic synth (11)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [Baud Girl FM-1+VA](https://baudgirl.com/work/FM-1+VA) | Stock FM-1 + virtual analog (Super 7-osc) + 8-bit | Stock 6-op FM, VA with ZDF filters, 8-bit engine with drums/game sounds | Your stock presets kept, VA presets, 8-bit drums | 64 steps, dot-matrix seq, Sync on ARP/SEQ pages | IN: USB, BLE, TRS. Clock in AND Clock Out setting. SysEx pattern writes. Full MIDI guide | closed source  |  | Closed source (free) ([installer](https://baudgirl.com/work/FM-1+VA/install)) | Closed |
| [DUELL](https://github.com/oscillr/DUELL) | Bi-timbral performance synth (Roland JV / Korg layer-split era) | 12 engines, two independent parts, morph | ~100 sounds, 16 multi-setups, 16 patterns | Per-part arpeggiators, 16 patterns | Per-part channel, program change, bank select, clock sync, CC for morph. Sidechain duck via MIDI | quiet 2026-10-14 | 7 | Prebuilt .fwsc (beta) ([installer](https://oscillr.github.io/DUELL/install/)) | GPL-3.0 |
| [ETCH](https://github.com/SikkenWorks/ETCH) | Wave-drawing synth (Fairlight / Casio FZ spirit) | Drawn single-cycle waves A/B morph + C modulator, 8 voices | Wave library | Motion rec, arp with RIFF mode | USB | quiet 2026-10-14 | 5 | Web installer ([installer](https://etch.sikkenworks.com/)) | GPL-3.0 |
| [FM-106](https://github.com/patttf/fm-106) | Roland Juno-106 | KR-106 port: 6-voice DCO, chorus | 2 factory + 2 user banks, Juno .syx import via web Librarian | None (synth) | USB in, USB-C audio out | quiet 2026-10-14 | 8 | Web installer ([installer](https://patttf.github.io/fm-106/Librarian.html)) | GPL-3.0 |
| [Golana](https://github.com/Gadlele/Golana) | Korg microKORG (MS-20 filter) | 4-voice VA, 2 osc, dual LFO, patch matrix, 24/12 dB LPF, BPF, HPF, MS-20 LPF | Programs with on-screen waveform/filter drawing | 16-step per program, arp | USB in | quiet 2026-10-14 | 0 | Build from source | GPL-3.0 |
| [Lunar Modulator](https://github.com/ip2k/lunar-modulator) | Mutable Instruments Plaits + Movy sequencer | 5 Mutable-derived engines, 160+ models | Models, shapes and patches | Step seq with p-locks | USB (browser only so far) | quiet 2026-10-14 | 59 | Emulator only | MIT |
| [Melodee](https://github.com/keremimo/melodee) | Sequential Prophet-5 Rev4, Casio CZ-1, Commodore SID, Yamaha DX7 | PROPHET (2 osc, SSI/Curtis filters, poly-mod), CZ-1 phase distortion, SID, FM6, DRUM | 200 Prophet-5 factory programs, 64 CZ-1 factory tones, 64 DX7 slots, 70 microtonal tunings, .syx import/export | 4 tracks, 32 pattern banks, 1024 notes, note editor, QNT | IN: USB + TRS, ch 1-4 tracks, ch 10 drums. Clock INT/USB/TRS + Start/Stop/Continue. OUT: USB notes. SysEx preset import | quiet 2026-10-14 | 74 | Web installer ([installer](https://keremimo.github.io/melodee/)) | GPL-3.0 |
| [Modular-1](https://wiggismodular.github.io/Modular-1/) | Clavia Nord Modular | Patchable modules, mod matrix | Your own patches from the browser editor | Euclidean generative arp | USB | n/a  |  | Web installer ([installer](https://wiggismodular.github.io/Modular-1/)) | GPL-3.0 |
| [OberVave](https://github.com/zvenson/obervave) | Oberheim OB-Xa / OB-8 | 8-voice VA, 2 osc, sync, X-mod, SEM/Curtis morphing filter, drift, unison | OB-style programs | None (synth) | USB | quiet 2026-10-14 | 5 | Web installer ([installer](https://fm1.designburgapps.com/)) | GPL-3.0 |
| [SLOOP DX7 Banks](https://github.com/majnikool/sloop-fm1) | DX7 preset browser on SLOOP | SLOOP FM6 | 12 categorized DX7 banks = 384 voices | SLOOP | USB | quiet 2026-10-09 | 1 | Build from source | GPL-3.0 |
| [sloopDX](https://github.com/zvenson/dxsloop) | Yamaha DX7 + FM drum machine | Dexed msfa 6-op FM (32 alg) + resonant LPF, FM drums | 256 .syx voices (8 banks), 20 modern patches, 5 FM kits x 16 sounds | 128 steps/track, p-locks, OMNI chord harp | SLOOP MIDI stack (USB + TRS) | quiet 2026-10-14 | 22 | Web installer ([installer](https://dx7.designburgapps.com/)) | GPL-3.0 |

## Groovebox (22)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [AMBII](https://github.com/JalopyMusic/fm1-milkboyg-ambii) | Melodee with a performance UI | Melodee core | Melodee | 4 tracks, automation graphs, undo | USB | quiet 2026-10-10 | 0 | Emulator only | GPL-3.0 |
| [Felucca](https://github.com/hugelton/Felucca) | Original multi-engine groovebox (OP-Z / Dirtywave M8 spirit) | 13: ANALOG (2 osc VA), DIGITAL (4-op FM), PHASE (Casio PD), LOFI (chiptune), SAMPLE, VOICE (formant), TRIO (3 osc), WHEEL (tonewheel organ), GRAIN, FM6 (DX7), PHYS, SLICE, NOISE | Factory presets per engine, GM drum track, user sample slots, DX7 .syx import | 4 tracks / 8 voices, 64 steps, chords, ties, slides, live rec, per-track slicer | IN: USB + TRS, per-track channel, MIDI LEARN. OUT: USB. Clock in 24 PPQN + Start/Stop. USB audio out | quiet 2026-10-14 | 479 | Web installer ([installer](https://hugelton.github.io/Felucca/)) | GPL-3.0 |
| [Felucca 8 Patterns](https://github.com/echoe/Felucca_8_patterns) | Felucca with song mode | Felucca minus SAMPLE | Felucca presets (no samples) | 8 chainable patterns per track | USB in | quiet 2026-10-14 | 3 | Prebuilt .fwsc | GPL-3.0 |
| [Felucca [Salt]](https://github.com/ChanceTheMaker/Felucca) | Felucca, polished | Felucca's 9-13 engines | 54 presets in Studio, Felucca factory sounds, favorites | Felucca 4-track 64-step | IN: USB + TRS with sustain, bend, modwheel, panic. Clock INT/USB/TRS + Start/Stop/Continue. On-device MIDI monitor. OUT: USB | quiet 2026-10-12 | 5 | Web installer ([installer](https://chancethemaker.github.io/Felucca/webapp/installer/)) | GPL-3.0 |
| [FM1 Move](https://github.com/Nicodesy06/FM1-MOVE) | Ableton Move | SLOOP 2.5 engines | SLOOP sounds + kits | 8 tracks, clips and scenes | USB | quiet 2026-10-14 | 8 | Emulator / experimental ([installer](https://nicodesy06.github.io/FM1-MOVE/device/)) | GPL-3.0 |
| [fm1-rocket-os](https://github.com/cmlarsen/fm1-rocket-os) | Ableton Live clip launcher | X0X/Felucca | X0X | Clip matrix (WIP) | USB | quiet 2026-10-12 | 1 | Work in progress | GPL-3.0 |
| [FM80S](https://github.com/y6zkcqnf5r-hue/fm1-fm80s) | Synthwave looper | SLOOP/Felucca | SLOOP | Loop stacking, song assembly | USB | quiet 2026-10-10 | 2 | Build from source | GPL-3.0 |
| [GHOULBOX 2.0](https://github.com/jasonpersinger/ghoulbox-fm1-dungeon-synth) | Dungeon synth rig (90s Casio/Roland + hurdy-gurdy) | Felucca engines + GURDY hurdy-gurdy, HALL reverb, TAPE/CRKL | 36+ dungeon sounds: crypt pads, monk choirs, lutes, organs; historical/just temperaments | Felucca 4-track, drone latching | USB in | quiet 2026-10-14 | 43 | Web installer ([installer](https://ghoulbox.messy.quest/webapp/installer/)) | GPL-3.0 |
| [Groove OS](https://www.groove-os.com/) | Elektron-style 8-track groovebox | 6-op FM (12 voices) + VA w/ ladder filter (8 voices) | Curated sound packs, DX7 .syx reception | 8 tracks, loop lengths 1-8 bars, 64 steps, p-locks, stage view | Per-track MIDI out channel, clock in + out | closed source  |  | Commercial ($29) ([installer](https://www.groove-os.com/)) | Proprietary |
| [Jangada](https://github.com/zednaked/jangada) | Industrial groovebox | 10 incl. 6-op FM, superwave analog | Custom drum kits, dark presets | 4 tracks, ratchets, drone modes | USB in | quiet 2026-10-14 | 26 | Web installer ([installer](https://zednaked.github.io/jangada/)) | GPL-3.0 |
| [JIANT FM](https://github.com/juanjiant-bit/JIANT) | Bio-synth groovebox, thermal-camera UI | 8: ANALOG, FM6, PHASE, LOFI bytebeat, VOICE, WHEEL, NOISE, DRUM-X | Presets per engine, 32 bytebeat formulas | 6 tracks, 8 songs x 4 sections, SL BUS slicer | USB | quiet 2026-10-14 | 112 | Web installer ([installer](https://juanjiant-bit.github.io/JIANT/webapp/installer/)) | GPL-3.0 |
| [MC-1](https://github.com/dspaudio/mc-1) | Roland D-50 (LA synthesis) + MC-303 | LA synthesis (PCM attack + synth sustain), TR drums, 303 acid | LA presets, TR voices | 4 lanes: drums, bass, chords, lead/arp | USB | quiet 2026-10-14 | 1 | Web installer ([installer](https://dspaudio.github.io/mc-1-web/)) | GPL-3.0 |
| [NoteSorcery](https://github.com/catacombius/NoteSorcery) | OP-1 8-track + Ableton bridge | SLOOP | Live USB sampling | 8 tracks, export to Ableton .als | USB, Android app | quiet 2026-10-09 | 1 | Build from source | GPL-3.0 |
| [ORBIT](https://github.com/dspaudio/orbit) | Teenage Engineering OP-1 | SLOOP engines | SLOOP + sample tools | 4 tracks, event tape | USB | quiet 2026-10-12 | 18 | Web installer | GPL-3.0 |
| [Polly](https://github.com/charlesvestal/fm1-polly) | Yamaha QY70 arranger | Sonivox EAS General MIDI | Full GM bank, accompaniment styles, QY style import | 8 arranger tracks, chord follower, fills, intro/outro | USB in; GM via MIDI IN | quiet 2026-10-14 | 10 | Web installer ([installer](https://charlesvestal.github.io/fm1-polly/)) | GPL-3.0 |
| [REDACTED](https://fm1-redacted-installer.xrhetor.chatgpt.site/) | Lo-fi noise box | PULSE, VOLTAGE, STATIC, GHOST layers | Fractured lo-fi layers | 4 tracks, FRACTURE/STATIC/CHANCE/MUTATE macros | USB in | n/a  |  | Web installer ([installer](https://fm1-redacted-installer.xrhetor.chatgpt.site/)) | GPL-3.0 |
| [Skiff](https://github.com/illuminus5/skiff) | Elektron Digitakt-style sequencer | 14: VA, FM, wavetable, physical, drums, noise | Factory presets per engine | 6 tracks, 64 steps, p-locks, microtiming, ratchets, trig conditions | USB in | quiet 2026-10-13 | 3 | Web installer ([installer](https://illuminus5.github.io/skiff/webapp/installer/)) | GPL-3.0 |
| [SLOOP](https://github.com/isod89/sloop-fm1) | Teenage Engineering OP-Z / Elektron live groovebox | 12: analog, FM, 6-op FM w/ DX7 import, physical, noise, drums | 153 sounds, 37 drum kits, user samples, user presets | 4 tracks (3 synth + drums), 64 steps, p-locks, microtiming, fills, swing, song A-D | IN: USB + TRS. Clock USB/TRS + Start/Continue/Stop, clock-only mode. OUT: sequencer notes (OUT=SEQ). USB audio in | quiet 2026-10-13 | 485 | Web installer ([installer](https://isod89.github.io/sloop-fm1/)) | GPL-3.0 |
| [SLOOP ALG](https://github.com/shaw-core/Sloop_ALG02) | SLOOP + extra synthesis | Karplus-Strong, plucked, additive, DX7, VA | SLOOP | SLOOP | USB | quiet 2026-10-07 | 3 | Web installer | GPL-3.0 |
| [SLOOP Floyd FM](https://github.com/renebohne/sloop-fm1) | SLOOP + 4-op FM (Floyd Steinberg) | 4-op FM w/ custom matrices | SLOOP + FM | SLOOP, live scope | USB | quiet 2026-10-09 | 1 | Build from source | GPL-3.0 |
| [WaveLoop FM-1](https://github.com/ELI7VH/Felucca) | Felucca driven by an Arturia MiniLab 3 | Felucca engines | Felucca presets | Felucca 4-track + punch FX | IN: USB + TRS, MiniLab 3 fader/encoder map. Clock INT/USB/TRS. OUT: USB | quiet 2026-10-14 | 6 | Web installer ([installer](https://eli7vh.github.io/Felucca/)) | GPL-3.0 |
| [winampFM](https://github.com/hericdk/winampFM) | Winamp 2.x as a groovebox | SLOOP 2.6 engines | 157 sounds incl. cavaquinho, berimbau, agogô, sanfona, Brasil kits | SLOOP + tape looper w/ auto BPM, PARTY mode | USB | quiet 2026-10-14 | 5 | Web installer ([installer](https://hericdk.github.io/winampFM/)) | GPL-3.0 |

## Drum machine (6)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [BB1 (Big Beat)](https://github.com/TexasRADIO/bb1-firmware) | Two classic drum machines and a TB-303 in one box | 3: synthesised 808, sampled drum player, 303-style bass (Dillo) | 8 drum machines, 9 Dillo bass presets | Two independent drum layers + bass; catalogue parts up to 64 steps | IN: USB + TRS; default KIT A ch10, KIT B ch11, Dillo ch1; input clock/follow/transport settings. OUT: none | active 2026-10-29 | 0 | Web installer (1.5) ([installer](https://thebigbeat.app/fm1/install/)) | GPL-3.0 |
| [Bubba Machine](https://github.com/Erbubar23/bubba-machine) | TR drum machine + MPC-style sampler, written from scratch | TR drums (procedural), 8-slice sampler, wavetable bass, synth/mono/kit/MIDI tracks | All kits and wavetables synthesized in C, take library | 6 tracks, polymeter 1-64 steps, clock mult/div, 4 scenes, 16 punch FX | Internal clock only (so far); MIDI track type planned | quiet 2026-10-12 | 5 | Emulator only | GPL-3.0-or-later |
| [Hortator](https://github.com/DeadActive/hortator) | Roland TR-808/909 + Mutable Instruments Plaits drums + Grids | 808/909 models, Plaits drum models, user samples, resonators | Analog-model kits, user samples | 8 drum tracks, Grids generative patterns, fills, LFOs | IN: USB, TRS, BLE. Clock in all three + Start/Stop. Drum channel in GLO | quiet 2026-10-12 | 15 | Prebuilt .fwsc ([installer](https://deadactive.github.io/hortator/webapp/installer/)) | GPL-3.0 |
| [TRIBE](https://github.com/apiel/fm1-tribe) | Elektron-style clip groovebox with 909/808/303 | 25: KICK W/P, 909, 808, 303, zicBox scatter FX | Drum models + 303, scatter FX bank | 10 tracks, 16 clips each, 16-64 steps, 6 rates, 4 directions | USB in | quiet 2026-10-14 | 6 | Web installer ([installer](https://apiel.github.io/fm1-tribe/)) | GPL-3.0 |
| [X0X](https://github.com/charlesvestal/fm1-x0x) | Propellerhead ReBirth RB-338: Roland TR-909, TR-808, 2x TB-303 | 909 + 808 drum models, 2x 303 (schwung), breakbeat player | 909/808 kits, 303 acid generators (TB-3PO), breaks | 16 patterns, song mode, knob automation | USB in (Felucca stack) | quiet 2026-10-14 | 158 | Web installer ([installer](https://charlesvestal.github.io/fm1-x0x/install/)) | GPL-3.0 |
| [zp12](https://github.com/zvenson/zp12) | E-mu SP-12 / Linn 9000 era 12-bit sampler | 12-bit 26 kHz sample playback, rate-skip pitch, 8 channels w/ resonant filters | 32 pads x 4 banks, drop your own WAVs from the browser | 11 loops, 4 songs, 16-step grid, MPC swing 50-71%, 4 punch FX | USB | quiet 2026-10-14 | 24 | Web installer ([installer](https://zp12.designburgapps.com/)) | GPL-3.0 |

## Sampler (3)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [April OS](https://github.com/beashoko/april-os) | Pocket sampler (PO-33 KO spirit) | Sample playback + Felucca | 32 user sample slots x 3 s, record from phone/laptop mic | 8 tracks, slice/loop editor | USB in | quiet 2026-10-10 | 7 | Web installer ([installer](https://beashoko.github.io/april-os/)) | MIT |
| [FM-1 B-Boy Edition](https://github.com/friendsmakenoise-prog/fm1-pocket-sampler) | Late-90s hip-hop chop sampler (SP-1200 / MPC) | 3 sample tracks + FM bass/lead | User chops | Sample tracks | USB | REMOVED  |  | Web installer | None specified |
| [SLICE64-FM](https://jeymadcat-ops.github.io/SLICE64-FM-web/) | Beat slicer (SP-404 chop spirit) | 64-slice sampler + FM | User samples, transient detection | SLOOP | USB | n/a  |  | Web installer ([installer](https://jeymadcat-ops.github.io/SLICE64-FM-web/)) | GPL-3.0 |

## Chord instrument (4)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [ChoralRoot FM-1](https://github.com/Quixotic7/ChoralRootFM1) | Telepathic Orchid / Monome ChoralRoot | Felucca engines | Felucca presets; remix adds Prophet-5 (200) + BASS engine | Looper, performance bass line | USB in | quiet 2026-10-13 | 50 | Web installer ([installer](https://quixotic7.github.io/ChoralRootFM1/)) | GPL-3.0 |
| [fm1-chord](https://github.com/math0ne/fm1-chord) | Chord trainer / songwriting pad | Felucca | Felucca presets | Chord sequencer, accompaniment | MIDI in and out | quiet 2026-10-13 | 8 | Build from source | GPL-3.0 |
| [FoMni-1](https://github.com/charlesvestal/fm1-fomni) | Suzuki Omnichord | Harp strum + chord engine | Omnichord-style voices, rhythm accompaniment | Rhythm + arp modes | USB | quiet 2026-10-14 | 58 | Web installer ([installer](https://charlesvestal.github.io/fm1-fomni/)) | GPL-3.0 |
| [FuMi-1](https://github.com/cartesive/fumi-1) | Suikohsha ST-50 (Shigin) | FoMni | Koto, sho, shakuhachi, taiko in ST-50 just intonation | FoMni | USB | quiet 2026-10-13 | 7 | Web installer ([installer](https://cartesive.github.io/fumi-1/)) | GPL-3.0 |

## Physical model (1)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [FiMba-1](https://github.com/jadamsowers/fm1-fimba) | Kalimba / mbira / thumb piano | Physical model 44.1 kHz: tines, resonators, buzzers; granular cloud FX | Tine materials, gourd/box/board bodies | Mbira pattern generator, arp | USB | quiet 2026-10-13 | 17 | Web installer ([installer](https://jadamsowers.github.io/fm1-fimba/)) | GPL-3.0 |

## Generative (3)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [AMB-1](https://github.com/charlesvestal/fm1-amb) | Brian Eno tape-loop ambient | Loop model + bass + Euclidean perc | Generative | Unsynced tape loops, Euclidean | USB | quiet 2026-10-14 | 37 | Web installer ([installer](https://charlesvestal.github.io/fm1-amb/)) | GPL-3.0 |
| [FANTASMA / Pelucco](https://github.com/Gadlele/Pelucco) | Haunted ambient box + Omnichord | Felucca + BELL, AMBI reverb | Pads, lead, bells, sea/wind noise roles | 3-channel generator, BELL loops 13/17/23/29 steps | USB in. Rescue boot | quiet 2026-10-14 | 0 | Build from source | GPL-3.0 |
| [MAKU (幕間機)](https://github.com/okumurari2/maku) | Ambient intermission machine | DRUM, PHYS, GRAIN | Generated per boot, 16 saved 'liked' worlds | Generative, 70-90 BPM | IN: USB + TRS, clock follow, CC20 kick density | quiet 2026-10-14 | 20 | Prebuilt .fwsc ([installer](https://okumurari2.github.io/maku/)) | GPL-3.0 |

## Controller (2)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [CTL-1](https://github.com/charlesvestal/fm1-ctl) | MIDI keyboard controller (nanoKEY / Keystep spirit) | GM sounds for monitoring | General MIDI | Own-clock sequencer | OUT: keys as notes, knobs as CC in 4 banks, multi-channel, USB + TRS passthrough | quiet 2026-10-12 | 7 | Prebuilt .fwsc ([installer](https://charlesvestal.github.io/fm1-ctl/)) | GPL-3.0 |
| [FM-1 Macropad Patch](https://github.com/smememe/fm1-macropad-patch) | 55-input macro pad | None | None | None | OUT: every key/button/knob as USB-MIDI notes | n/a  |  | Web patcher ([installer](https://smememe.github.io/fm1-macropad-patch/)) | MIT |

## Factory (2)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [FM-1 Firmware Patcher](https://github.com/czietz/fm1-firmware-patcher) | Stock, DX7-accurate detune | Stock 6-op FM | Your stock presets | Stock | Stock, aftertouch disabled | n/a  |  | Script | Unlicense |
| [Stock V15 (M-VAVE)](https://www.m-vave.com/download) | Yamaha DX7 (6-op FM) | 6-op FM, 32 algorithms (Dexed/msfa-derived core) | 128 factory voices in 4 banks (A-D), DX7 .syx bank import, 6 FX | Arp + 16-step seq, 16 patterns, 30-300 BPM | IN: USB, BLE, TRS. OUT: notes only (USB/BLE). Clock in since V13, no clock out. CC 0-23 on FX channel | closed source  |  | Stock ([installer](https://www.m-vave.com/download)) | Proprietary |

## Platform / dev (6)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [Dinghy](https://github.com/zvenson/dinghy) | Developer skeleton | 4-voice sine demo | None | None | USB MIDI driver included | quiet 2026-10-12 | 28 | Build from source | GPL-3.0 |
| [FM1 Open Firmware (fm1_open)](https://github.com/m-vave/fm1_open) | Official SDK (8-track groovebox demo) | Vendor audio HAL + demo synth | 16 demo presets/FX, 8 sample slots | 8 tracks | USB MIDI | REMOVED  |  | Removed | GPL-3.0 (app) + vendor blobs |
| [fm1-polyseq](https://github.com/NOVALENTI/fm1-polyseq) | Bare-metal HAL | None (HAL) | None | Poly 16-step | USB | quiet 2026-09-04 | 2 | Build from source | None (source public) |
| [Hexagon Console](https://www.reddit.com/r/MVaveFM1/comments/1x5qq7z/coming_soon_hexagon_console/) | Unknown (teased) |  |  |  |  | announced only  |  | Teased | unknown |
| [Mocky](https://github.com/charlesvestal/fm1-mocky) | Display test tool |  |  |  | SysEx bitmaps | quiet 2026-10-10 | 2 | Web installer ([installer](https://charlesvestal.github.io/fm1-mocky/)) | GPL-3.0 |
| [Optimist](https://github.com/w0ts/optimist) | Build-your-own SLOOP | Pick from 13 engines at compile time | Pick kits/FX | SLOOP-style layers, scenes, p-locks | USB | quiet 2026-10-13 | 15 | Build from source (Docker) | GPL-3.0 |

## Kids (2)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [PurpleMonkey FM-1](https://github.com/Quixotic7/PurpleMonkeyFM1) | Toddler toy | Pentatonic synth + beats | 5-note scale, drum beats | Beats | USB | quiet 2026-10-10 | 2 | Web installer | GPL-3.0 |
| [Rainbow mode](https://github.com/joshbartlettband-web/felucca-rainbow) | Kids keyboard | Felucca + SFX | 40 animal sounds and rhythms, hidden full Felucca | Rhythms | USB in | quiet 2026-10-11 | 13 | Web installer ([installer](https://joshbartlettband-web.github.io/felucca-rainbow/)) | GPL-3.0 |

## Game / novelty (6)

| Firmware | Tries to be | Engines | Sounds | Sequencer | MIDI | Health | Stars | Install | License |
|---|---|---|---|---|---|---|---|---|---|
| [Fart Machine One](https://github.com/adamcharleswilsonmusic-code/Fart-Machine-One) | Joke sampler | Sample playback | 11 pitched fart samples | 16 steps | USB | quiet 2026-10-12 | 15 | Build from source | GPL-3.0 |
| [FM-1 Doom](https://github.com/zvenson/fm1doom) | Doom |  |  |  |  | quiet 2026-10-07 | 2 | Web installer ([installer](https://doom.deadlockinteractive.com/)) | GPL-2.0+/GPL-3.0 |
| [FM-1 NES](https://github.com/Keitark/fm1-nes) | Nintendo NES |  |  |  |  | quiet 2026-10-09 | 16 | Build from source | Apache-2.0 |
| [FM1 Quest](https://github.com/hericdk/fm1-quest) | SLOOP as an RPG | SLOOP | SLOOP | SLOOP (steps = attacks) | USB | quiet 2026-10-12 | 9 | Web installer ([installer](https://hericdk.github.io/fm1-quest/webapp/installer/)) | GPL-3.0 |
| [fm1-mdx](https://github.com/Keitark/fm1-mdx) | Sharp X68000 YM2151 player | YM2151 FM emulation | MDX/PDX files | Playback |  | quiet 2026-10-08 | 0 | Research | GPL-3.0 |
| [GameDude](https://github.com/ChanceTheMaker/gamedude-fm1-smk) | Nintendo Game Boy |  |  |  |  | quiet 2026-10-13 | 1 | Web installer ([installer](https://chancethemaker.github.io/gamedude-fm1-smk/)) | GPL-3.0 |

## Why each one exists

- **AMB-1** (Charles Vestal): Music for Airports in a box: unsynced tape loops of unequal lengths, gliding bass, Euclidean percussion, playing from power-on.
- **AMBII** (MilkBoyG / JalopyMusic): Alternative performance and recording interface on Melodee's engine core, with automation graphs and undo. Browser prototype, no hardware image yet.
- **April OS** (beashoko): Sampling first: 32 sample slots, slice and loop editor, record straight from a phone or laptop mic. Exists because stock has no sampling at all.
- **Baud Girl FM-1+VA** (Madeline (Baud Girl)): Keeps the stock FM engine and your presets but fixes the ergonomics, adds Virtual Analog (7-osc Super mode, ZDF filters), an 8-bit engine and a 64-step sequencer. The only free firmware documented with MIDI Clock Out.
- **BB1 (Big Beat)** (TexasRADIO): Two independent drum layers and Dillo, an Open303-derived monophonic acid bass, through shared tape echo and spring. Song sections, era grooves and an ACID phrase bank, with a browser player and web installer.
- **Bubba Machine** (Erbubar23): Written from scratch in C99 with zero third-party audio code, every kit procedurally synthesized. TR drum machine, 8-slice sampler, wavetable bass, polymeter per track. Hardware flasher still on the roadmap.
- **ChoralRoot FM-1** (Quixotic7): Ports the Monome-grid ChoralRoot chord engine: one hand picks roots, the other shapes voicings. Exists for chord-based live performance rather than step sequencing.
- **CTL-1** (Charles Vestal): Turns the FM-1 into a MIDI master controller: keys send notes, knobs send CC in four banks, TRS passed through, with GM sounds for monitoring. Exists so the FM-1 can drive your other synths.
- **Dinghy** (Sven Trogus (zvenson)): Minimal clean starting point for developers: 4-voice sine synth over working display, audio DMA, buttons and USB-MIDI. Start here to write your own firmware.
- **DUELL** (OSCILL/R (balinthcom)): Two full independent parts (LAYER / SPLIT / STEREO) with patch morphing between two states. Exists for multitimbral keyboard playing, something stock cannot do.
- **ETCH** (SikkenWorks): Draw single-cycle waves on the device, morph between them, modulate with a third. 8 voices, motion recording, generative RIFF arp.
- **FANTASMA / Pelucco** (Gadlele): Haunted generative ambient with Omnichord strum mode and very long AMBI reverb. Also introduced a built-in USB Rescue Boot (hold OCT- at power-on) so a bad flash is recoverable.
- **Fart Machine One** (adamcharleswilsonmusic-code): A joke firmware: 11 pitched flatulence samples, 16-step sequencer, delay and reverb. Proof the toolchain is easy enough for jokes.
- **Felucca** (Leo Kuroshita (Hügelton)): The root of the family tree. First complete open replacement OS: 13 engines, 4 tracks, 64-step sequencer, web editor, build guide. Nearly every other firmware forks this.
- **Felucca 8 Patterns** (echoe): Felucca 1.5.1 with 8 chainable patterns per track for song arrangement, paid for by dropping sample playback to free flash. Exists for arranging full songs.
- **Felucca [Salt]** (Chance Roth (ChanceTheMaker)): Felucca with the MIDI polish the base lacked: TRS input with full expression, selectable clock source, on-device MIDI monitor, 20 palettes, and a browser Studio that plays without hardware.
- **FiMba-1** (J. Adam Sowers): A thumb piano: detailed kalimba/mbira physical model at 44.1 kHz with tine, resonator and buzzer parameters, traditional tine layout, mbira pattern generator.
- **FM-1 B-Boy Edition** (friendsmakenoise-prog): Late-90s hip-hop chop sampler: 3 sample tracks plus an FM bass/lead lane.
- **FM-1 Doom** (Sven Trogus (zvenson)): Because it runs Doom. FreeDM arena map on the 240x240 screen, keys and knobs as controls, keeps sloopDX projects intact.
- **FM-1 Firmware Patcher** (Christian Zietz (czietz)): Keeps stock but fixes the detune calculation to match a real DX7 and disables aftertouch (which caused heavy vibrato from many controllers). Recolors the UI so you know it is patched.
- **FM-1 Macropad Patch** (smememe): Turns stock into a 55-input USB-MIDI macro pad: every button, key and knob sends a note, LEDs off. For desktop hotkey software.
- **FM-1 NES** (Keitark): NES emulator and, more usefully, a worked example of writing bare-metal FM-1 firmware and app-only updates that preserve the bootloader.
- **FM-106** (PattF): A Roland Juno-106 (KR-106 engine port): 6 voices on both cores, oscilloscope split screen, .syx patch import, USB audio out. Exists for one classic polysynth done well.
- **FM1 Move** (Nicodesy06): Ableton Move workflow on the FM-1: 8 tracks, clips and scenes instead of a linear song arranger, custom 240x240 UI. Hardware verification still in progress.
- **FM1 Open Firmware (fm1_open)** (M-VAVE): M-VAVE's own short-lived open-source release of the firmware and SDK (board drivers, audio HAL, WASM workbench). Pulled offline, but its leak of HAL code accelerated the whole scene.
- **FM1 Quest** (hericdk): SLOOP as a fantasy sidescroller: tracks are party heroes, steps are attacks, BPM is walk speed, recording triggers boss fights. Exists for fun.
- **fm1-chord** (math0ne): Chord composition tool, chord sequencer, rhythm accompanist and ear trainer. Exists as a songwriting and practice aid rather than a performance box.
- **fm1-mdx** (Keitark): Sharp X68000 MDX chiptune player with YM2151 emulation, part muting and live accompaniment. Research project.
- **fm1-polyseq** (NOVALENTI): A strict-C99 bare-metal HAL for the AC791N with a polyphonic 16-step sequencer. Exists as a clean-room developer foundation.
- **fm1-rocket-os** (cmlarsen): Ableton-style clip launcher and matrix sequencer forked from X0X.
- **FM80S** (Floydus): Synthwave-oriented synth-looper for stacking loops into songs, with planned 8-track expansion.
- **FoMni-1** (Charles Vestal): A Suzuki Omnichord: strum white keys like a harp plate, pick chord root and type on black keys, with rhythm accompaniment. Exists for non-keyboardists.
- **FuMi-1** (cartesive): FoMni fork recreating the Suikohsha ST-50 Japanese Shigin accompaniment instrument with koto, sho, shakuhachi and taiko in historical just intonation.
- **GameDude** (Chance The Maker): Drop a .gb ROM in the browser, get a flashable firmware. Peanut-GB core on the FM-1 and SMK-37.
- **GHOULBOX 2.0** (Jason Persinger): A genre firmware: dungeon synth and dark ambient. Cathedral HALL reverb, worn-cassette tape stage, a hurdy-gurdy engine, historical temperaments, RPG-styled UI.
- **Golana** (Gadlele): Recreates the Korg microKORG workflow and MATRIX editing, with live waveform and filter-curve drawing on screen. Exists for people who want one deep virtual-analog synth.
- **Groove OS** (Groove OS): Paid polished groovebox: up to 8 tracks with independent loop lengths, 6-op FM + VA ladder-filter engines, 20 voices, p-locks, stage view. Exists as the turnkey commercial option.
- **Hexagon Console** (unknown): Teased hexagonal-UI performance console. Nothing released yet.
- **Hortator** (DEADACTIVE): A dedicated drum machine. 808/909 and Mutable Plaits drum models, Grids generative rhythms, user samples, pumping compressor. Fills the gap for people who want the FM-1 as a drum brain next to other synths.
- **Jangada** (zednaked): Dark, industrial, Brazilian-accented take on Felucca with ratchets, drone modes and custom kits. Exists as a personal sound-design flavor of the platform.
- **JIANT FM** (juanjiant-bit): Thermal-camera themed 6-track OS where each engine behaves like an organism. Adds bytebeat/floatbeat LOFI with 32 formulas and a mix-bus slicer.
- **Lunar Modulator** (ip2k): Brings Mutable Instruments engines (Plaits-style models, 160+) and a Movy-style sequencer with p-locks to the FM-1. Still browser-only, not flashable yet.
- **MAKU (幕間機)** (okumurari2): Always-on generative ambience for DJ intermissions: power on and an in-key evolving soundscape is already playing. Buttons are verbs that nudge the world; REC saves worlds you like.
- **MC-1** (dspaudio): Roland D-50 Linear Arithmetic synthesis (PCM attack + synthesized sustain) in an MC-303 style 4-track groovebox with TR drums and 303 acid.
- **Melodee** (Kerem Kilic (keremimo)): Felucca rebuilt around classic polysynths: a real Prophet-5 Rev4 model with all 200 factory programs, a Casio CZ-1 engine, SID, and microtonal FM6. For people who want a vintage synth, not a groovebox.
- **Mocky** (Charles Vestal): Push arbitrary bitmaps to the screen over WebMIDI. A UI mockup and display testing tool for firmware developers.
- **Modular-1** (morgulbrut (wiggismodular)): Patch a modular synth in the browser and upload it to the FM-1, with a Euclidean generative arpeggiator. Exists for modular-minded sound design.
- **NoteSorcery** (catacombius): OP-1 style 8 tracks with live USB sampling and project export straight into Ableton Live sets, plus an Android controller app. Exists to bridge the FM-1 into a DAW workflow.
- **OberVave** (Sven Trogus (zvenson)): An 8-voice Oberheim OB-Xa / OB-8 style polysynth: dual osc, sync, cross-mod, morphing 12/24 dB filter, voice drift, unison. One classic American poly.
- **Optimist** (w0ts): Pick your own engines, kits, FX and sequencer features at compile time to fit flash/RAM budgets. SLOOP 2.4 project compatible. Exists because 1 MB flash forces trade-offs.
- **ORBIT** (dspaudio): SLOOP with Teenage Engineering OP-1 visuals, sample tools and an event tape for shifting what tracks play. Exists for the OP-1 aesthetic.
- **Polly** (Charles Vestal): A Yamaha QY70 in your pocket: 8-track arranger with chord recognition, styles, fills, intro/outro and QY style import on a General MIDI engine. Exists for songwriters who want a backing band.
- **PurpleMonkey FM-1** (Quixotic7): Zero-menu toddler toy: 5-note pentatonic scale and backing beats.
- **Rainbow mode** (joshbartlettband-web): A children's instrument: rainbow color-coded keys, 40 animal sounds, safe volume limiter, with the full Felucca hidden behind a secret key combo.
- **REDACTED** (DJ Redacted): Experimental fractured lo-fi box with performance macros FRACTURE / STATIC / CHANCE / MUTATE on the top knobs. A vibe firmware with a broken-vinyl splash screen.
- **Skiff** (illuminus5): Felucca with more tracks and an Elektron-style sequencer: p-locks, microtiming, ratchets, trig conditions. Exists for deep step-sequencing.
- **SLICE64-FM** (jeymadcat-ops): Beat-slicing box: 64 slices across keys with transient detection, reverse and per-slice pitch, plus FM accompaniment.
- **SLOOP** (isod89): The second big platform. A live groovebox for any style with no mandatory presets: 3 synth tracks + drums, 64 steps, song mode, USB audio in, web editor with backup/restore. Most mature and most forked after Felucca.
- **SLOOP ALG** (shaw-core): Experimental fork adding Karplus-Strong strings, plucked models, additive synthesis, DX7 and VA to SLOOP.
- **SLOOP DX7 Banks** (majnikool): SLOOP with 12 categorized DX7 banks (384 voices) in flash for instant preset browsing without touching your project.
- **SLOOP Floyd FM** (René Bohne): Adds Floyd Steinberg's 4-operator FM algorithms and a live scope/envelope display to SLOOP.
- **sloopDX** (Sven Trogus (zvenson)): SLOOP workflow plus a sample-identical Dexed msfa DX7 engine, a resonant filter behind every voice, and a programmable 16x8 FM drum machine. For DX7 purists who still want a groovebox.
- **Stock V15 (M-VAVE)** (M-VAVE): The factory firmware. 6-op DX7-style FM, 128 presets, ARP and 16-step SEQ. The baseline every mod is measured against and the required starting point (V15) before flashing anything else.
- **TRIBE** (Alexandre Piel (apiel)): X0X taken further: 10 freely assignable tracks, 25 engines, 16 clips per track, scatter FX from zicBox. Exists for Elektron-style clip-based live techno.
- **WaveLoop FM-1** (ELI7VH): Felucca tuned for being driven by an Arturia MiniLab 3: faders to tracks, encoders follow track, DJ filter, punch-in FX pads. Exists for external-controller performance.
- **winampFM** (hericdk): SLOOP 2.6 dressed as Winamp 2.x: playlist preset browser, EQ-slider FX, tape looper, 28 pixel-art visualizers, Brazilian instruments. Exists for nostalgia and party performance.
- **X0X** (Charles Vestal): A ReBirth RB-338 in your pocket: 909, 808, two 303s with acid generators and a breakbeat player, all at once. Built because the FM-1's form factor begged for a drum-machine box.
- **zp12** (Sven Trogus (zvenson)): An authentic 80s 12-bit drum sampler (SP-12 / Linn spirit): 26 kHz, rate-skipping pitch with no interpolation, 8 cut channels with decaying filters, MPC swing. Drop your own WAVs from the browser.
