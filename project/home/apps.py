from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

# @ app.route('/fertilizer-predict', methods=['POST'])
# def fert_recommend():
#     title = 'Harvestify - Fertilizer Suggestion'

#     crop_name = str(request.form['cropname'])
#     N = int(request.form['nitrogen'])
#     P = int(request.form['phosphorous'])
#     K = int(request.form['pottasium'])
#     # ph = float(request.form['ph'])

#     df = pd.read_csv('Data/fertilizer.csv')

#     nr = df[df['Crop'] == crop_name]['N'].iloc[0]
#     pr = df[df['Crop'] == crop_name]['P'].iloc[0]
#     kr = df[df['Crop'] == crop_name]['K'].iloc[0]

#     n = nr - N
#     p = pr - P
#     k = kr - K
#     temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
#     max_value = temp[max(temp.keys())]
#     if max_value == "N":
#         if n < 0:
#             key = 'NHigh'
#         else:
#             key = "Nlow"
#     elif max_value == "P":
#         if p < 0:
#             key = 'PHigh'
#         else:
#             key = "Plow"
#     else:
#         if k < 0:
#             key = 'KHigh'
#         else:
#             key = "Klow"

#     response = Markup(str(fertilizer_dic[key]))

#     return render_template('fertilizer-result.html', recommendation=response, title=title)
