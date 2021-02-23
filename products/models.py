from django.db import models

CHARITIES = [
    ('Marie Curie', 'Marie Curie'),
    ('Animal Welfare Fund', 'Animal Welfare Fund'),
    ('GiveWel', 'GiveWell'),
    ('Against Malaria Foundation', 'Against Malaria Foundation'),
    ('Development Media International', 'Development Media International'),
    ('Evidence Action', 'Evidence Action'),
    ('Fistula Foundation', 'Fistula Foundation'),
    ('Fred Hollows Foundation', 'Fred Hollows Foundation'),
    ('GiveDirectly', 'GiveDirectly'),
    ('Helen Keller International', 'Helen Keller International'),
    ('Innovations for Proverty Action', 'Innovations for Proverty Action'),
    ('Iodine Global Network', 'Iodine Global Network'),
    ('Living Goods', 'Living Goods'),
    ('Malaria Consortium', 'Malaria Consortium'),
    ('New Incentives', 'New Incentives'),
    ('One Acre Fund', 'One Acre Fund'),
    ('Oxfam', 'Oxfam'),
    ('Population Services International', 'Population Services International'),
    ('Project Healthy Children', 'Project Healthy Children'),
    ('SCI Foundation', 'SCI Foundation'),
    ('Seva', 'Seva'),
    ('Village Enterprise', 'Village Enterprise'),
    ('Zusha!', 'Zusha!'),
    ('Macmillan Cancer Support', 'Macmillan Cancer Support'),
    ('Cancer Research UK', 'Cancer Research UK'),
    ('St. John Ambulance', 'St. John Ambulance'),
    ('Great Ormond Street Hospital', 'Great Ormond Street Hospital'),
    ('Samaritans', 'Samaritans'),
    ('British Red Cross', 'British Red Cross'),
    ('British Heart Foundation', 'British Heart Foundation'),
    ('RSPCA', 'RSPCA'),
    ("Alzheimer's Research UK", "Alzheimer's Research UK"),
    ('RNLI Lifeboats', 'RNLI Lifeboats'),
    ('Guide Dogs', 'Guide Dogs'),
    ('WWF', 'WWF'),
    ("Alzheimer's Society", "Alzheimer's Society"),
    ('NSPCC', 'NSPCC'),
    ('RSPB', 'RSPB'),
    ('Age UK', 'Age UK'),
    ('National Trust', 'National Trust'),
    ('Keep Britain Tidy', 'Keep Britain Tidy'),
    ('Battersea Dogs and Cats Home', 'Battersea Dogs and Cats Home'),
    ('Prostate Cancer UK', 'Prostate Cancer UK'),
    ('Dementia UK', 'Dementia UK'),
    ('Children in Need', 'Children in Need'),
    ('Mind', 'Mind'),
    ('Help for Heroes', 'Help for Heroes'),
    ('Dogs Trust', 'Dogs Trust'),
    ('Save the Children', 'Save the Children'),
    ('Salvation Army', 'Salvation Army'),
    ("Barnardo's", "Barnardo's"),
    ('The Fairtrade Foundation', 'The Fairtrade Foundation'),
    ('Comic Relief', 'Comic Relief'),
    ('Teenage Cancer Trust', 'Teenage Cancer Trust'),
    ('Diabetes UK', 'Diabetes UK'),
    ('UNICEF', 'UNICEF'),
    ('Bowel Cancer UK', 'Bowel Cancer UK'),
    ('Hearing Dogs for Deaf People', 'Hearing Dogs for Deaf People'),
    ('Prince of Wales Trust', 'Price of Wales Trust'),
    ('Breast Cancer Care', 'Breast Cancer Care'),
    ('PDSA', 'PDSA'),
    ('The Donkey Sanctuary', 'The Donkey Sanctuary'),
    ('Shelter', 'Shelter'),
    ("Parkinson's UK", "Parkinson's UK"),
]

sorted_charities = sorted(CHARITIES)

class Product(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    charity = models.CharField(
        max_length=254,
        choices=sorted_charities,
        default = '',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
