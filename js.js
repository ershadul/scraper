// Provide a default path to dwr.engine
2if (typeof this['dwr'] == 'undefined') this.dwr = {};
3if (typeof dwr['engine'] == 'undefined') dwr.engine = {};
4if (typeof dwr.engine['_mappedClasses'] == 'undefined') dwr.engine._mappedClasses = {};
5
6if (window['dojo']) dojo.provide('dwr.interface.context');
7
8if (typeof this['context'] == 'undefined') context = {};
9
10context._path = '/dwr';
11
12/**
13 * @param {class java.lang.String} p2 a param
14 * @param {function|Object} callback callback function or options object
15 */
16context.updateCountryAndCurrency = function(p2, callback) {
17 return dwr.engine._execute(context._path, 'context', 'updateCountryAndCurrency', arguments);
18};