# Generated by Django 4.1.7 on 2023-03-25 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("program_categories", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Program",
            fields=[
                ("title", models.CharField(max_length=150, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=150, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True)),
                ("views_count", models.PositiveBigIntegerField(default=0)),
                (
                    "region",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Afghanistan", "Afghanistan"),
                            ("land Islands", "land Islands"),
                            ("Albania", "Albania"),
                            ("Algeria", "Algeria"),
                            ("American Samoa", "American Samoa"),
                            ("AndorrA", "AndorrA"),
                            ("Angola", "Angola"),
                            ("Anguilla", "Anguilla"),
                            ("Antarctica", "Antarctica"),
                            ("Antigua and Barbuda", "Antigua and Barbuda"),
                            ("Argentina", "Argentina"),
                            ("Armenia", "Armenia"),
                            ("Aruba", "Aruba"),
                            ("Australia", "Australia"),
                            ("Austria", "Austria"),
                            ("Azerbaijan", "Azerbaijan"),
                            ("Bahamas", "Bahamas"),
                            ("Bahrain", "Bahrain"),
                            ("Bangladesh", "Bangladesh"),
                            ("Barbados", "Barbados"),
                            ("Belarus", "Belarus"),
                            ("Belgium", "Belgium"),
                            ("Belize", "Belize"),
                            ("Benin", "Benin"),
                            ("Bermuda", "Bermuda"),
                            ("Bhutan", "Bhutan"),
                            ("Bolivia", "Bolivia"),
                            ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
                            ("Botswana", "Botswana"),
                            ("Bouvet Island", "Bouvet Island"),
                            ("Brazil", "Brazil"),
                            (
                                "British Indian Ocean Territory",
                                "British Indian Ocean Territory",
                            ),
                            ("Brunei Darussalam", "Brunei Darussalam"),
                            ("Bulgaria", "Bulgaria"),
                            ("Burkina Faso", "Burkina Faso"),
                            ("Burundi", "Burundi"),
                            ("Cambodia", "Cambodia"),
                            ("Cameroon", "Cameroon"),
                            ("Canada", "Canada"),
                            ("Cape Verde", "Cape Verde"),
                            ("Cayman Islands", "Cayman Islands"),
                            ("Central African Republic", "Central African Republic"),
                            ("Chad", "Chad"),
                            ("Chile", "Chile"),
                            ("China", "China"),
                            ("Christmas Island", "Christmas Island"),
                            ("Cocos (Keeling), Islands", "Cocos (Keeling), Islands"),
                            ("Colombia", "Colombia"),
                            ("Comoros", "Comoros"),
                            ("Congo", "Congo"),
                            (
                                "CongoThe Democratic Republic of the",
                                "CongoThe Democratic Republic of the",
                            ),
                            ("Cook Islands", "Cook Islands"),
                            ("Costa Rica", "Costa Rica"),
                            ("Cote D'Ivoire", "Cote D'Ivoire"),
                            ("Croatia", "Croatia"),
                            ("Cuba", "Cuba"),
                            ("Cyprus", "Cyprus"),
                            ("Czech Republic", "Czech Republic"),
                            ("Denmark", "Denmark"),
                            ("Djibouti", "Djibouti"),
                            ("Dominica", "Dominica"),
                            ("Dominican Republic", "Dominican Republic"),
                            ("Ecuador", "Ecuador"),
                            ("Egypt", "Egypt"),
                            ("El Salvador", "El Salvador"),
                            ("Equatorial Guinea", "Equatorial Guinea"),
                            ("Eritrea", "Eritrea"),
                            ("Estonia", "Estonia"),
                            ("Ethiopia", "Ethiopia"),
                            (
                                "Falkland Islands (Malvinas),",
                                "Falkland Islands (Malvinas),",
                            ),
                            ("Faroe Islands", "Faroe Islands"),
                            ("Fiji", "Fiji"),
                            ("Finland", "Finland"),
                            ("France", "France"),
                            ("French Guiana", "French Guiana"),
                            ("French Polynesia", "French Polynesia"),
                            (
                                "French Southern Territories",
                                "French Southern Territories",
                            ),
                            ("Gabon", "Gabon"),
                            ("Gambia", "Gambia"),
                            ("Georgia", "Georgia"),
                            ("Germany", "Germany"),
                            ("Ghana", "Ghana"),
                            ("Gibraltar", "Gibraltar"),
                            ("Greece", "Greece"),
                            ("Greenland", "Greenland"),
                            ("Grenada", "Grenada"),
                            ("Guadeloupe", "Guadeloupe"),
                            ("Guam", "Guam"),
                            ("Guatemala", "Guatemala"),
                            ("Guernsey", "Guernsey"),
                            ("Guinea", "Guinea"),
                            ("Guinea-Bissau", "Guinea-Bissau"),
                            ("Guyana", "Guyana"),
                            ("Haiti", "Haiti"),
                            (
                                "Heard Island and Mcdonald Islands",
                                "Heard Island and Mcdonald Islands",
                            ),
                            (
                                "Holy See (Vatican City State),",
                                "Holy See (Vatican City State),",
                            ),
                            ("Honduras", "Honduras"),
                            ("Hong Kong", "Hong Kong"),
                            ("Hungary", "Hungary"),
                            ("Iceland", "Iceland"),
                            ("India", "India"),
                            ("Indonesia", "Indonesia"),
                            ("IranIslamic Republic Of", "IranIslamic Republic Of"),
                            ("Iraq", "Iraq"),
                            ("Ireland", "Ireland"),
                            ("Isle of Man", "Isle of Man"),
                            ("Israel", "Israel"),
                            ("Italy", "Italy"),
                            ("Jamaica", "Jamaica"),
                            ("Japan", "Japan"),
                            ("Jersey", "Jersey"),
                            ("Jordan", "Jordan"),
                            ("Kazakhstan", "Kazakhstan"),
                            ("Kenya", "Kenya"),
                            ("Kiribati", "Kiribati"),
                            (
                                "KoreaDemocratic People'S Republic of",
                                "KoreaDemocratic People'S Republic of",
                            ),
                            ("KoreaRepublic of", "KoreaRepublic of"),
                            ("Kuwait", "Kuwait"),
                            ("Kyrgyzstan", "Kyrgyzstan"),
                            (
                                "Lao People'S Democratic Republic",
                                "Lao People'S Democratic Republic",
                            ),
                            ("Latvia", "Latvia"),
                            ("Lebanon", "Lebanon"),
                            ("Lesotho", "Lesotho"),
                            ("Liberia", "Liberia"),
                            ("Libyan Arab Jamahiriya", "Libyan Arab Jamahiriya"),
                            ("Liechtenstein", "Liechtenstein"),
                            ("Lithuania", "Lithuania"),
                            ("Luxembourg", "Luxembourg"),
                            ("Macao", "Macao"),
                            (
                                "MacedoniaThe Former Yugoslav Republic of",
                                "MacedoniaThe Former Yugoslav Republic of",
                            ),
                            ("Madagascar", "Madagascar"),
                            ("Malawi", "Malawi"),
                            ("Malaysia", "Malaysia"),
                            ("Maldives", "Maldives"),
                            ("Mali", "Mali"),
                            ("Malta", "Malta"),
                            ("Marshall Islands", "Marshall Islands"),
                            ("Martinique", "Martinique"),
                            ("Mauritania", "Mauritania"),
                            ("Mauritius", "Mauritius"),
                            ("Mayotte", "Mayotte"),
                            ("Mexico", "Mexico"),
                            (
                                "MicronesiaFederated States of",
                                "MicronesiaFederated States of",
                            ),
                            ("MoldovaRepublic of", "MoldovaRepublic of"),
                            ("Monaco", "Monaco"),
                            ("Mongolia", "Mongolia"),
                            ("Montenegro", "Montenegro"),
                            ("Montserrat", "Montserrat"),
                            ("Morocco", "Morocco"),
                            ("Mozambique", "Mozambique"),
                            ("Myanmar", "Myanmar"),
                            ("Namibia", "Namibia"),
                            ("Nauru", "Nauru"),
                            ("Nepal", "Nepal"),
                            ("Netherlands", "Netherlands"),
                            ("Netherlands Antilles", "Netherlands Antilles"),
                            ("New Caledonia", "New Caledonia"),
                            ("New Zealand", "New Zealand"),
                            ("Nicaragua", "Nicaragua"),
                            ("Niger", "Niger"),
                            ("Nigeria", "Nigeria"),
                            ("Niue", "Niue"),
                            ("Norfolk Island", "Norfolk Island"),
                            ("Northern Mariana Islands", "Northern Mariana Islands"),
                            ("Norway", "Norway"),
                            ("Oman", "Oman"),
                            ("Pakistan", "Pakistan"),
                            ("Palau", "Palau"),
                            (
                                "Palestinian TerritoryOccupied",
                                "Palestinian TerritoryOccupied",
                            ),
                            ("Panama", "Panama"),
                            ("Papua New Guinea", "Papua New Guinea"),
                            ("Paraguay", "Paraguay"),
                            ("Peru", "Peru"),
                            ("Philippines", "Philippines"),
                            ("Pitcairn", "Pitcairn"),
                            ("Poland", "Poland"),
                            ("Portugal", "Portugal"),
                            ("Puerto Rico", "Puerto Rico"),
                            ("Qatar", "Qatar"),
                            ("Reunion", "Reunion"),
                            ("Romania", "Romania"),
                            ("Russian Federation", "Russian Federation"),
                            ("RWANDA", "RWANDA"),
                            ("Saint Helena", "Saint Helena"),
                            ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
                            ("Saint Lucia", "Saint Lucia"),
                            ("Saint Pierre and Miquelon", "Saint Pierre and Miquelon"),
                            (
                                "Saint Vincent and the Grenadines",
                                "Saint Vincent and the Grenadines",
                            ),
                            ("Samoa", "Samoa"),
                            ("San Marino", "San Marino"),
                            ("Sao Tome and Principe", "Sao Tome and Principe"),
                            ("Saudi Arabia", "Saudi Arabia"),
                            ("Senegal", "Senegal"),
                            ("Serbia", "Serbia"),
                            ("Seychelles", "Seychelles"),
                            ("Sierra Leone", "Sierra Leone"),
                            ("Singapore", "Singapore"),
                            ("Slovakia", "Slovakia"),
                            ("Slovenia", "Slovenia"),
                            ("Solomon Islands", "Solomon Islands"),
                            ("Somalia", "Somalia"),
                            ("South Africa", "South Africa"),
                            (
                                "South Georgia and the South Sandwich Islands",
                                "South Georgia and the South Sandwich Islands",
                            ),
                            ("Spain", "Spain"),
                            ("Sri Lanka", "Sri Lanka"),
                            ("Sudan", "Sudan"),
                            ("Suriname", "Suriname"),
                            ("Svalbard and Jan Mayen", "Svalbard and Jan Mayen"),
                            ("Swaziland", "Swaziland"),
                            ("Sweden", "Sweden"),
                            ("Switzerland", "Switzerland"),
                            ("Syrian Arab Republic", "Syrian Arab Republic"),
                            ("TaiwanProvince of China", "TaiwanProvince of China"),
                            ("Tajikistan", "Tajikistan"),
                            (
                                "TanzaniaUnited Republic of",
                                "TanzaniaUnited Republic of",
                            ),
                            ("Thailand", "Thailand"),
                            ("Timor-Leste", "Timor-Leste"),
                            ("Togo", "Togo"),
                            ("Tokelau", "Tokelau"),
                            ("Tonga", "Tonga"),
                            ("Trinidad and Tobago", "Trinidad and Tobago"),
                            ("Tunisia", "Tunisia"),
                            ("Turkey", "Turkey"),
                            ("Turkmenistan", "Turkmenistan"),
                            ("Turks and Caicos Islands", "Turks and Caicos Islands"),
                            ("Tuvalu", "Tuvalu"),
                            ("Uganda", "Uganda"),
                            ("Ukraine", "Ukraine"),
                            ("United Arab Emirates", "United Arab Emirates"),
                            ("United Kingdom", "United Kingdom"),
                            ("United States", "United States"),
                            (
                                "United States Minor Outlying Islands",
                                "United States Minor Outlying Islands",
                            ),
                            ("Uruguay", "Uruguay"),
                            ("Uzbekistan", "Uzbekistan"),
                            ("Vanuatu", "Vanuatu"),
                            ("Venezuela", "Venezuela"),
                            ("Viet Nam", "Viet Nam"),
                            ("Virgin IslandsBritish", "Virgin IslandsBritish"),
                            ("Virgin IslandsU.S.", "Virgin IslandsU.S."),
                            ("Wallis and Futuna", "Wallis and Futuna"),
                            ("Western Sahara", "Western Sahara"),
                            ("Yemen", "Yemen"),
                            ("Zambia", "Zambia"),
                            ("Zimbabwe", "Zimbabwe"),
                        ],
                        max_length=50,
                    ),
                ),
                ("donations_goal", models.FloatField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="charity_programs",
                        to="program_categories.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="charity_programs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Programs",
            },
        ),
    ]
