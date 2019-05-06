
import * as d3 from 'd3'

export default class Controller {

    static displayData(d, data) {
        var word = d.word,
            count = d.count,
            channels;

        channels = d.mentions;

        var container = d3.select('div.selected')

        container.select('.word')
            .html(word.charAt(0).toUpperCase() + word.slice(1))
            .append('span')
            .attr('class', 'count')
            .html(count + ' times, ' + d.mentions.length + ' channels')

        container.select('.channels')
            .selectAll('div.article').remove()

        container.select('.channels')
            .selectAll('div.article').data(channels)
            .enter().append('div')
            .attr('class', 'article')
            .html((article) => article.title)
            .append('span')
            .attr('class', 'count')
            .html((article) => article.count + ' times')

        container.select('.channels')
            .selectAll('span')
            .html((article) => article.count + ' times')

        container.select('.channels')
            .selectAll('div.article').data(channels)
            .exit().remove()
    }

}
