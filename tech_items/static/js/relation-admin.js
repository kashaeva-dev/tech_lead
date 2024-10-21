django.jQuery(document).ready(function() {
    var relationTypeSelect = django.jQuery('#id_relation_type');
    var outItemSelect = django.jQuery('#id_out_item');
    var inItemSelect = django.jQuery('#id_in_item');

    function updateOutItemOptions() {
        var relationTypeId = relationTypeSelect.val();
        var selectedValue = outItemSelect.val();  // Сохраняем текущее выбранное значение
        if (relationTypeId) {
            django.jQuery.ajax({
                url: '/ajax/filter-out-item/',
                data: {
                    'relation_type': relationTypeId
                },
                dataType: 'json',
                success: function(data) {
                    var items = data.items;
                    outItemSelect.empty();

                    // Добавляем пустой вариант
                    outItemSelect.append(
                        django.jQuery('<option></option>').attr('value', '').text('---------')
                    );

                    for (var i = 0; i < items.length; i++) {
                        var item = items[i];
                        outItemSelect.append(
                            django.jQuery('<option></option>').attr('value', item.id).text(item.name)
                        );
                    }

                    // Проверяем, есть ли сохраненное значение в новом списке опций
                    if (items.some(item => item.id == selectedValue)) {
                        outItemSelect.val(selectedValue);  // Устанавливаем сохраненное значение
                    } else {
                        outItemSelect.val('');  // Если нет, устанавливаем пустое значение
                    }
                },
                error: function(xhr, status, error) {
                    console.error('AJAX Error (out_item):', status, error);
                }
            });
        } else {
            outItemSelect.empty();
            outItemSelect.append(
                django.jQuery('<option></option>').attr('value', '').text('---------')
            );
            outItemSelect.val('');
        }
    }

    function updateInItemOptions() {
        var relationTypeId = relationTypeSelect.val();
        var selectedValue = inItemSelect.val();  // Сохраняем текущее выбранное значение
        if (relationTypeId) {
            django.jQuery.ajax({
                url: '/ajax/filter-in-item/',
                data: {
                    'relation_type': relationTypeId
                },
                dataType: 'json',
                success: function(data) {
                    var items = data.items;
                    inItemSelect.empty();

                    // Добавляем пустой вариант
                    inItemSelect.append(
                        django.jQuery('<option></option>').attr('value', '').text('---------')
                    );

                    for (var i = 0; i < items.length; i++) {
                        var item = items[i];
                        inItemSelect.append(
                            django.jQuery('<option></option>').attr('value', item.id).text(item.name)
                        );
                    }

                    // Проверяем, есть ли сохраненное значение в новом списке опций
                    if (items.some(item => item.id == selectedValue)) {
                        inItemSelect.val(selectedValue);  // Устанавливаем сохраненное значение
                    } else {
                        inItemSelect.val('');  // Если нет, устанавливаем пустое значение
                    }
                },
                error: function(xhr, status, error) {
                    console.error('AJAX Error (in_item):', status, error);
                }
            });
        } else {
            inItemSelect.empty();
            inItemSelect.append(
                django.jQuery('<option></option>').attr('value', '').text('---------')
            );
            inItemSelect.val('');
        }
    }

    // Обновляем оба поля при изменении типа связи
    relationTypeSelect.change(function() {
        updateOutItemOptions();
        updateInItemOptions();
    });

    // Вызываем функции обновления при загрузке страницы, если тип связи уже выбран
    if (relationTypeSelect.val()) {
        updateOutItemOptions();
        updateInItemOptions();
    }
});
