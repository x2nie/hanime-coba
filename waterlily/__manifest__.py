{
   "name":  "water lily",
   "version":   "2.0",
   "category":  "Service/view menu",
   "sequence":  20,
   "author":    "₊˚ reii ⊹♡",
   "license":   "LGPL-3",
   "summary":   "my experimental module :)", 
   "depends":   [
        "point_of_sale",
        "base_setup",
        "resource",
        "mail",
        "web",
        "web_tour",
        "digest",
        "rating",
   ],
   "data":  [
         "views/res_config_settings.xml"  
   ],
   'assets': {
        'web.assets_backend': [
            "waterlily/static/lib/**/*.css",
            "waterlily/static/src/style.css",
        ]
   },
    "images": [
        "static/description/banner.png",
        "static/theme_screenshot.png"
    ]
}