from io import BytesIO

import pandas as pd
from django.http import HttpResponse


def export_csv(self):
    data = self.get_export_data()
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="car_reports.csv"'

    countries_df = pd.DataFrame(
        [{'ID': c.id, 'Название': c.name} for c in data['countries']])
    countries_df.to_csv(response, index=False, encoding='utf-8-sig')
    response.write('\n\n--- ПРОИЗВОДИТЕЛИ ---\n\n')

    manufacturers_df = pd.DataFrame([
        {'ID': m.id, 'Название': m.name, 'Страна': m.country.name}
        for m in data['manufacturers']
    ])
    manufacturers_df.to_csv(response, index=False,
                            encoding='utf-8-sig', mode='a')
    response.write('\n\n--- АВТОМОБИЛИ ---\n\n')

    cars_df = pd.DataFrame([
        {
            'ID': c.id,
            'Название': c.name,
            'Производитель': c.manufacturer.name,
            'Страна': c.manufacturer.country.name,
            'Год начала': c.start_year,
            'Год окончания': c.end_year or 'Настоящее время'
        }
        for c in data['cars']
    ])
    cars_df.to_csv(response, index=False, encoding='utf-8-sig', mode='a')
    response.write('\n\n--- КОММЕНТАРИИ ---\n\n')

    comments_df = pd.DataFrame([
        {
            'ID': c.id,
            'Email автора': c.author_email,
            'Автомобиль': c.car.name,
            'Производитель': c.car.manufacturer.name,
            'Дата создания': c.created_at.strftime('%Y-%m-%d %H:%M'),
            'Комментарий': c.text
        }
        for c in data['comments']
    ])
    comments_df.to_csv(response, index=False,
                       encoding='utf-8-sig', mode='a')

    return response


def export_xlsx(self):
    data = self.get_export_data()
    output = BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df = pd.DataFrame([{'ID': c.id, 'Название': c.name}
                           for c in data['countries']])
        df.to_excel(writer, sheet_name='Страны', index=False)
        df = pd.DataFrame([
            {'ID': m.id, 'Название': m.name, 'Страна': m.country.name}
            for m in data['manufacturers']
        ])
        df.to_excel(writer, sheet_name='Производители', index=False)
        df = pd.DataFrame([
            {
                'ID': c.id,
                'Название': c.name,
                'Производитель': c.manufacturer.name,
                'Страна': c.manufacturer.country.name,
                'Год начала': c.start_year,
                'Год окончания': c.end_year or 'Настоящее время'
            }
            for c in data['cars']
        ])
        df.to_excel(writer, sheet_name='Автомобили', index=False)

        df = pd.DataFrame([
            {
                'ID': c.id,
                'Email автора': c.author_email,
                'Автомобиль': c.car.name,
                'Производитель': c.car.manufacturer.name,
                'Дата создания': c.created_at.strftime('%Y-%m-%d %H:%M'),
                'Комментарий': c.text
            }
            for c in data['comments']
        ])
        df.to_excel(writer, sheet_name='Комментарии', index=False)

    output.seek(0)
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="car_reports.xlsx"'
    return response
