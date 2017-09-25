from django.db import models
from django.core.validators import URLValidator

from multiselectfield import MultiSelectField


LANGS_CHOICES = [
    ('ja', '日本語'),
    ('ko', '韓国語'),
    ('cn', '中国語'),
    ('en', '英語'),
    ('ar', 'アラビア語'),
    ('bn', 'ベンガル語'),
    ('cs', 'チェコ語'),
    ('da', 'デンマーク語'),
    ('de', 'ドイツ語'),
    ('el', 'ギリシア語'),
    ('es', 'スペイン語'),
    ('fa', 'ペルシア語'),
    ('fi', 'フィンランド語'),
    ('fr', 'フランス語'),
    ('he', 'ヘブライ語'),
    ('hi', 'ヒンディー語'),
    ('hu', 'ハンガリー語'),
    ('id', 'インドネシア語'),
    ('it', 'イタリア語'),
    ('nl', 'オランダ語'),
    ('no', 'ノルウェー語'),
    ('pl', 'ポーランド語'),
    ('pt', 'ポルトガル語'),
    ('ro', 'ルーマニア語'),
    ('ru', 'ロシア語'),
    ('sv', 'スウェーデン語'),
    ('th', 'タイ語'),
    ('tr', 'トルコ語'),
    ('uk', 'ウクライナ語'),
    ('ur', 'ウルドゥー語'),
    ('vi', 'ベトナム語'),
]


class Onedraw(models.Model):
    name = models.CharField(max_length=30, help_text='Twitter アカウントのユーザー名')
    screen_name = models.CharField(max_length=15, primary_key=True,
                                   help_text='Twitter アカウントの @ユーザー名')
    work = models.CharField(max_length=30, help_text='ワンドロの対象の作品名')
    genre = models.CharField(max_length=30, help_text='作品内の CP 名など')
    event_day = models.CharField(max_length=30, help_text='開催日 (曜日や週など)')
    rule_url = models.CharField(max_length=300, validators=[URLValidator], blank=True,
                                help_text='ワンドロのルールや注意事項が書かれたページの URL')
    rt_screen_name = models.CharField(max_length=15, blank=True,
                                      help_text='参加ツイートをリツイートするアカウント の @ユーザー名')
    collection_url = models.CharField(max_length=300, validators=[URLValidator], blank=True,
                                help_text='ツイートまとめページの URL')
    langs = MultiSelectField(choices=LANGS_CHOICES, help_text='対応している言語')
    active = models.BooleanField(default=True, help_text='活動中であるかどうか')
    description = models.TextField(blank=True, help_text='補足説明')
