define([
    'jquery',
    'widgets/js/widget'
], function ($, widget) {

    var _getId = (function () {

            var cnt = 0;
            return function () {

                cnt += 1;
                return 'fileupload_' + cnt;
            }
    })();

    'use strict';
    var FileUploadView = widget.DOMWidgetView.extend({

        render: function render () {

            FileUploadView.__super__.render.apply(this, arguments);
            var id = _getId();
            var $label = $('<label />')
            .text('Browse')
            .addClass('btn btn-default')
            .attr('for', id)
            .appendTo(this.$el);

            $('<input />')
            .attr('type', 'file')
            .attr('id', id)
            .css('display', 'none')
            .appendTo($label);
        },

        events: {
            'change': '_handleFileChange'
        },

        _handleFileChange: function _handleFileChange (ev) {

            var file = ev.target.files[0];
            var that = this;
            if (file) {
                var fileReader = new FileReader();
                fileReader.onload = function fileReaderOnload () {

                    that.model.set('data_base64', fileReader.result);
                    that.touch();
                };
                fileReader.readAsDataURL(file);
            }
            else {
                that.send({ event: 'Unable to open file.' });
            }
            that.model.set('filename', file.name);
            that.touch();
        }
    });

    return { FileUploadView: FileUploadView };
});
