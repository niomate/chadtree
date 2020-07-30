from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, auto
from typing import Dict, Optional, Sequence, Set

Index = Set[str]
Selection = Set[str]


class Mode(IntEnum):
    orphan_link = auto()
    link = auto()
    sticky_writable = auto()
    sticky_dir = auto()
    folder = auto()
    block_device = auto()
    char_device = auto()
    door = auto()
    executable = auto()
    multi_hardlink = auto()
    other_writable = auto()
    pipe = auto()
    set_gid = auto()
    set_uid = auto()
    socket = auto()
    file_w_capacity = auto()
    file = auto()


@dataclass(frozen=True)
class Node:
    path: str
    mode: Set[Mode]
    name: str
    children: Optional[Dict[str, Node]] = None
    ext: Optional[str] = None


@dataclass(frozen=True)
class Session:
    index: Index


@dataclass(frozen=True)
class IconSet:
    active: str
    selected: str
    folder_open: str
    folder_closed: str
    link: str
    link_broken: str
    filetype: Dict[str, str]
    filename: Dict[str, str]
    quickfix_hl: str
    version_ctl_hl: str


@dataclass(frozen=True)
class UpdateTime:
    min_time: float
    max_time: float


@dataclass(frozen=True)
class VersionControlOptions:
    defer: bool


@dataclass(frozen=True)
class HLgroup:
    name: str
    cterm: Set[str] = field(default_factory=set)
    ctermfg: Optional[str] = None
    ctermbg: Optional[str] = None
    guifg: Optional[str] = None
    guibg: Optional[str] = None


@dataclass(frozen=True)
class HLcontext:
    groups: Sequence[HLgroup]
    mode_lookup_pre: Dict[Mode, HLgroup]
    mode_lookup_post: Dict[Optional[Mode], HLgroup]
    name_lookup: Dict[str, HLgroup]


@dataclass(frozen=True)
class Settings:
    follow: bool
    hl_context: HLcontext
    icons: IconSet
    keymap: Dict[str, Sequence[str]]
    name_ignore: Sequence[str]
    open_left: bool
    path_ignore: Sequence[str]
    session: bool
    show_hidden: bool
    update: UpdateTime
    use_icons: bool
    version_ctl: VersionControlOptions
    width: int


@dataclass(frozen=True)
class QuickFix:
    locations: Dict[str, int]


@dataclass(frozen=True)
class VCStatus:
    ignored: Set[str] = field(default_factory=set)
    status: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Highlight:
    begin: int
    end: int
    group: str


@dataclass(frozen=True)
class Badge:
    text: str
    group: str


@dataclass(frozen=True)
class Render:
    line: str
    badges: Sequence[Badge]
    highlights: Sequence[Highlight]


@dataclass(frozen=True)
class State:
    index: Index
    selection: Selection
    show_hidden: bool
    follow: bool
    width: int
    root: Node
    qf: QuickFix
    vc: VCStatus
    current: Optional[str]
    lookup: Sequence[Node]
    rendered: Sequence[Render]
