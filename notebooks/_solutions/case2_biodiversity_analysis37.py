(pn.ggplot(month_evolution.reset_index(name='count'), 
           pn.aes(x='eventDate', y='count', color='name'))
    + pn.geom_line()
    + pn.facet_wrap('name', nrow=4)
    + pn.theme_light()
)